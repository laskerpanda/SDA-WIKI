# Ingest System

**SDA Commons Wiki · South High School**

The ingest system converts raw source documents into structured wiki entries. Every wiki entry links back to its original source document.

---

## How to Ingest a Document

**Option 1 — Tell Hermes via Telegram:**
```
Process this PDF into a reading library entry: [drop file or paste URL]
```

**Option 2 — Drop in RAW_INTAKE and ask Hermes:**
```
Process RAW_INTAKE/reading_library/[filename.pdf] into a reading library entry for Era 3.
```

**Option 3 — Project Gutenberg (public domain texts):**
```
Add to reading library: Common Sense by Thomas Paine (Project Gutenberg)
```

Hermes will fetch the plain text, generate the structured entry, and commit it to the wiki.

---

## Source Document Storage

All source documents are stored in `~/sda-wiki/RAW_INTAKE/` and linked from wiki entries. Every reading library entry must include a **Source** field pointing to either:

1. A file path in RAW_INTAKE (for PDFs you own)
2. A public URL (Project Gutenberg, Avalon Project, etc.)
3. A note that a school library copy is required (copyrighted texts)

---

## Ingest Queue

Current files awaiting processing:

| File | Type | Target |
|------|------|--------|
| `RAW_INTAKE/fps_frames/` | FPS Framers | Standards pages |
| `RAW_INTAKE/standards/` | Standards docs | Standards pages |
| `RAW_INTAKE/reading_library/` | PDFs | Reading library entries |
| `RAW_INTAKE/skinnies_raw/` | Standard descriptions | Skinnies |

---

## Source URLs for Public Domain Texts

These texts are freely available and can be ingested directly:

| Text | Source URL |
|------|-----------|
| Common Sense — Paine | gutenberg.org/ebooks/147 |
| Magna Carta | avalon.law.yale.edu/medieval/magframe.asp |
| Declaration of Rights of Man | avalon.law.yale.edu/18th_century/rightsof.asp |
| Vindication of Rights of Woman — Wollstonecraft | gutenberg.org/ebooks/3420 |
| Communist Manifesto | gutenberg.org/ebooks/61 |
| Narrative of Frederick Douglass | gutenberg.org/ebooks/23 |
| MLK Letter from Birmingham Jail | africa.upenn.edu/Articles_Gen/Letter_Birmingham.html |
| UN Declaration of Human Rights | un.org/en/about-us/universal-declaration-of-human-rights |
| Analects of Confucius | gutenberg.org/ebooks/4094 |
| Haitian Declaration of Independence | thelouvertureproject.org |

---

## What a Processed Entry Looks Like

Every reading library entry must have:

```markdown
**Source:** [URL or file path — always a real link to the original document]
```

If it's a copyrighted text (Night, 1984, etc.):
```markdown
**Source:** School library copy required — not available digitally
**Excerpts at:** [any legally available excerpt source]
```

---

*Ingest System · SDA Commons Wiki · South High School*
*See also: [Resource Bank](index.md) · [Primary Sources](primary-sources/index.md) · [Reading Library](../reading-library/index.md)*
