#!/usr/bin/env python3
"""
generate_quote_image.py — Create styled quote images for picture frame display.
No API key required. Uses Pillow only.

Usage:
    python3 generate_quote_image.py --quote "TEXT" --author "NAME" --category CATEGORY --output PATH

Categories: Continental_Philosophy, Historical_Eras, Severus_Snape
"""

import argparse
import textwrap
import os
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
except ImportError:
    print("ERROR: Pillow not installed. Run: pip install Pillow")
    raise

# ── Style definitions per category ──────────────────────────────────────────

STYLES = {
    "Continental_Philosophy": {
        "bg_color": (18, 22, 28),          # near-black blue-grey
        "text_color": (230, 220, 200),     # warm cream
        "author_color": (160, 140, 100),   # muted gold
        "rule_color": (80, 70, 50),        # dim gold
        "quote_size": 52,
        "author_size": 32,
        "label": "CONTINENTAL PHILOSOPHY",
        "label_color": (60, 80, 70),
    },
    "Historical_Eras": {
        "bg_color": (42, 35, 25),          # dark parchment/sepia
        "text_color": (225, 210, 175),     # aged cream
        "author_color": (180, 150, 90),    # old gold
        "rule_color": (100, 80, 50),       # sepia rule
        "quote_size": 52,
        "author_size": 32,
        "label": "HISTORICAL ERAS",
        "label_color": (70, 55, 35),
    },
    "Severus_Snape": {
        "bg_color": (8, 14, 10),           # near-black green
        "text_color": (210, 220, 210),     # cool white-green
        "author_color": (80, 140, 100),    # Slytherin green
        "rule_color": (30, 70, 45),        # dark green rule
        "quote_size": 52,
        "author_size": 32,
        "label": "SEVERUS SNAPE",
        "label_color": (30, 60, 40),
    },
}

DEFAULT_STYLE = {
    "bg_color": (20, 20, 20),
    "text_color": (230, 230, 230),
    "author_color": (150, 150, 120),
    "rule_color": (70, 70, 50),
    "quote_size": 52,
    "author_size": 32,
    "label": "QUOTE",
    "label_color": (60, 60, 60),
}

# ── Font loading ─────────────────────────────────────────────────────────────

def find_font(size, bold=False, italic=False):
    """Try to load a good system font, fall back to default."""
    candidates = []
    if italic and bold:
        candidates = [
            "/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSerif-BoldItalic.ttf",
            "/usr/share/fonts/truetype/freefont/FreeSerifBoldItalic.ttf",
        ]
    elif italic:
        candidates = [
            "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf",
            "/usr/share/fonts/truetype/freefont/FreeSerifItalic.ttf",
        ]
    elif bold:
        candidates = [
            "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
        ]
    else:
        candidates = [
            "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
            "/usr/share/fonts/truetype/freefont/FreeSerif.ttf",
            "/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf",
        ]

    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)

    # Last resort: Pillow's built-in bitmap font
    return ImageFont.load_default()


# ── Core drawing ─────────────────────────────────────────────────────────────

def make_quote_image(quote: str, author: str, category: str, width=1920, height=1080) -> Image.Image:
    style = STYLES.get(category, DEFAULT_STYLE)

    img = Image.new("RGB", (width, height), style["bg_color"])
    draw = ImageDraw.Draw(img)

    # Subtle vignette overlay
    vignette = Image.new("RGB", (width, height), (0, 0, 0))
    vig_draw = ImageDraw.Draw(vignette)
    for i in range(min(width, height) // 3):
        alpha = int(120 * (i / (min(width, height) // 3)))
        vig_draw.rectangle([i, i, width - i, height - i], outline=(0, 0, 0, alpha))
    img = Image.blend(img, vignette, alpha=0.15)
    draw = ImageDraw.Draw(img)

    margin = int(width * 0.1)
    text_width = width - 2 * margin
    center_x = width // 2
    center_y = height // 2

    # ── Quote text ──
    quote_font = find_font(style["quote_size"], italic=True)
    label_font = find_font(22)
    author_font = find_font(style["author_size"])

    # Wrap quote to fit width
    avg_char_w = style["quote_size"] * 0.55
    wrap_width = max(20, int(text_width / avg_char_w))
    wrapped = textwrap.fill(f'"{quote}"', width=wrap_width)
    lines = wrapped.split("\n")

    line_height = style["quote_size"] + 14
    total_quote_h = len(lines) * line_height

    # Calculate vertical layout
    rule_gap = 20
    author_gap = 30
    total_h = total_quote_h + rule_gap + 2 + rule_gap + author_gap + style["author_size"]
    start_y = center_y - total_h // 2

    # Draw quote lines
    y = start_y
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=quote_font)
        tw = bbox[2] - bbox[0]
        draw.text((center_x - tw // 2, y), line, font=quote_font, fill=style["text_color"])
        y += line_height

    # Rule
    y += rule_gap
    rule_w = min(400, text_width // 2)
    draw.line(
        [(center_x - rule_w // 2, y), (center_x + rule_w // 2, y)],
        fill=style["rule_color"],
        width=2,
    )
    y += rule_gap + author_gap

    # Author
    author_text = f"— {author}" if author else ""
    if author_text:
        bbox = draw.textbbox((0, 0), author_text, font=author_font)
        tw = bbox[2] - bbox[0]
        draw.text((center_x - tw // 2, y), author_text, font=author_font, fill=style["author_color"])

    # Category label (bottom right, subtle)
    label_text = style["label"]
    bbox = draw.textbbox((0, 0), label_text, font=label_font)
    lw = bbox[2] - bbox[0]
    draw.text(
        (width - margin - lw, height - 50),
        label_text,
        font=label_font,
        fill=style["label_color"],
    )

    return img


# ── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Generate styled quote image for picture frame")
    parser.add_argument("--quote", required=True, help="The quote text")
    parser.add_argument("--author", default="", help="Author name")
    parser.add_argument(
        "--category",
        default="Continental_Philosophy",
        choices=list(STYLES.keys()),
        help="Style category",
    )
    parser.add_argument("--output", required=True, help="Output PNG path")
    parser.add_argument("--width", type=int, default=1920)
    parser.add_argument("--height", type=int, default=1080)
    args = parser.parse_args()

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    img = make_quote_image(args.quote, args.author, args.category, args.width, args.height)
    img.save(str(output_path), "PNG", quality=95)
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
