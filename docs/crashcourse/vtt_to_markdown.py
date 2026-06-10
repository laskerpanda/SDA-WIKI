#!/usr/bin/env python3
"""
vtt_to_markdown.py
------------------
Convert YouTube auto-generated VTT subtitle files into clean plain-text paragraphs
suitable for wiki entries.

Usage:
    # Single file
    python3 vtt_to_markdown.py episode.vtt

    # Whole directory
    python3 vtt_to_markdown.py /path/to/vtt/directory/

    # Explicit output file
    python3 vtt_to_markdown.py episode.vtt -o episode.md

Output is written to stdout unless -o is specified.
When processing a directory, output files are written alongside each VTT as .md files.
"""

import re
import sys
import os
import textwrap
import argparse
from pathlib import Path


# ---------------------------------------------------------------------------
# Cleaning helpers
# ---------------------------------------------------------------------------

# Timestamp line pattern: 00:00:00.000 --> 00:00:03.000
TIMESTAMP_RE = re.compile(r"^\d{2}:\d{2}:\d{2}[.,]\d{3}\s+-->\s+\d{2}:\d{2}:\d{2}[.,]\d{3}")

# VTT cue settings (align, position, line, etc.)
CUE_SETTINGS_RE = re.compile(r"\s+(align|position|line|size|vertical):\S+")

# Inline tags: <00:00:01.200>, <c>, </c>, <i>, </i>, <b>, </b>, <u>, </u>
INLINE_TAG_RE = re.compile(r"<[^>]+>")

# Noise patterns to strip or replace
NOISE_PATTERNS = [
    # Music / sound cues
    (re.compile(r"\[Music\]", re.IGNORECASE), ""),
    (re.compile(r"\[Applause\]", re.IGNORECASE), ""),
    (re.compile(r"\[Laughter\]", re.IGNORECASE), ""),
    (re.compile(r"\[.*?\]"), ""),           # Any remaining bracketed cues

    # Speaker indicators like >>> or >>
    (re.compile(r"^>>+\s*"), ""),

    # Lone dashes used as filler
    (re.compile(r"^\s*-\s*$"), ""),

    # Non-breaking spaces and other unicode whitespace
    (re.compile(r"\xa0"), " "),

    # Multiple spaces
    (re.compile(r" {2,}"), " "),
]


def clean_line(line: str) -> str:
    """Strip a single VTT caption line of all markup and noise."""
    line = INLINE_TAG_RE.sub("", line)
    line = CUE_SETTINGS_RE.sub("", line)
    for pattern, replacement in NOISE_PATTERNS:
        line = pattern.sub(replacement, line)
    return line.strip()


def parse_vtt(text: str) -> list[str]:
    """
    Parse raw VTT content and return a list of cleaned caption strings.
    Duplicate consecutive lines (YouTube repeats the previous cue in the next
    cue block) are deduplicated here.
    """
    lines = text.splitlines()
    captions = []
    prev = None

    i = 0
    # Skip the WEBVTT header
    while i < len(lines) and not lines[i].strip().startswith("WEBVTT"):
        i += 1
    i += 1  # skip the WEBVTT line itself

    while i < len(lines):
        line = lines[i]

        # Skip blank lines, cue index numbers, and timestamp lines
        if not line.strip():
            i += 1
            continue
        if line.strip().isdigit():
            i += 1
            continue
        if TIMESTAMP_RE.match(line.strip()):
            i += 1
            continue

        cleaned = clean_line(line)
        if cleaned and cleaned != prev:
            captions.append(cleaned)
            prev = cleaned
        i += 1

    return captions


def captions_to_paragraphs(captions: list[str], min_sentence_len: int = 60) -> str:
    """
    Join caption fragments into readable paragraphs.

    Strategy:
    - Join all fragments into one string.
    - Re-split on sentence-ending punctuation to create natural paragraph breaks.
    - Wrap each paragraph to ~100 chars.
    """
    # Join with spaces
    raw = " ".join(captions)

    # Normalize whitespace
    raw = re.sub(r"\s+", " ", raw).strip()

    # Split into sentences (naive but good enough for CC transcripts)
    # Split after . ! ? followed by a space and uppercase letter
    sentence_re = re.compile(r"(?<=[.!?])\s+(?=[A-Z])")
    sentences = sentence_re.split(raw)

    # Group sentences into paragraphs of ~4-6 sentences each
    paragraphs = []
    group = []
    for sent in sentences:
        group.append(sent.strip())
        if len(group) >= 5:
            paragraphs.append(" ".join(group))
            group = []
    if group:
        paragraphs.append(" ".join(group))

    # Wrap each paragraph
    wrapped = []
    for para in paragraphs:
        if para:
            wrapped.append(textwrap.fill(para, width=100))

    return "\n\n".join(wrapped)


def vtt_file_to_markdown(vtt_path: Path) -> str:
    """
    Convert a single VTT file to a clean markdown transcript block.
    Returns the markdown string.
    """
    text = vtt_path.read_text(encoding="utf-8", errors="replace")
    captions = parse_vtt(text)
    if not captions:
        return "_No transcript content found in this VTT file._"
    return captions_to_paragraphs(captions)


def process_file(vtt_path: Path, output_path: Path | None = None) -> None:
    """Process a single VTT file. Print to stdout or write to output_path."""
    md = vtt_file_to_markdown(vtt_path)
    if output_path:
        output_path.write_text(md, encoding="utf-8")
        print(f"  Wrote: {output_path}", file=sys.stderr)
    else:
        print(md)


def process_directory(dir_path: Path) -> None:
    """Process all VTT files in a directory, writing .md files alongside them."""
    vtt_files = sorted(dir_path.glob("*.vtt"))
    if not vtt_files:
        print(f"No .vtt files found in {dir_path}", file=sys.stderr)
        return
    for vtt_path in vtt_files:
        md_path = vtt_path.with_suffix(".md")
        print(f"Converting: {vtt_path.name}", file=sys.stderr)
        process_file(vtt_path, md_path)
    print(f"\nDone. Converted {len(vtt_files)} VTT file(s).", file=sys.stderr)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Convert YouTube VTT subtitle files to clean markdown text.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "input",
        help="Path to a .vtt file OR a directory containing .vtt files",
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file path (only valid when input is a single file). "
             "Defaults to stdout.",
        default=None,
    )
    args = parser.parse_args()

    input_path = Path(args.input)

    if not input_path.exists():
        print(f"Error: '{input_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    if input_path.is_dir():
        if args.output:
            print("Warning: -o is ignored when processing a directory.", file=sys.stderr)
        process_directory(input_path)
    elif input_path.is_file():
        output_path = Path(args.output) if args.output else None
        process_file(input_path, output_path)
    else:
        print(f"Error: '{input_path}' is not a file or directory.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
