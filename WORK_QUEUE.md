# SDA Wiki — Hermes Work Queue
# Last updated: 2026-06-10
# Purpose: Hermes reads this file to know what to build next.
# Update status inline as you work. Commit after every completed item.

---

## HOW TO USE THIS FILE

Pick the highest-priority PENDING item. Do it. Change its status to DONE. Commit. Move to the next.
If you're blocked, mark BLOCKED and add a note. Notify Reese via Telegram.

---

## PRIORITY 1 — Wiki Cross-Linking Pass (Remaining Standards Pages)

All era and unit pages need the same treatment already done on era-1-civilizations.md.
Each page needs 4 new sections appended before the footer:
- **Skinnies for [Era/Unit]** — links to actual skinny files in `skinnies/` (only link if file exists)
- **Reading Library — [Era/Unit] Texts** — links to reading library entries
- **CrashCourse Episodes** — links to crashcourse entries
- **Related Standards** — ELA standards most used in this era/unit

| Task | File | Status |
|------|------|--------|
| Cross-link Era 2 | docs/standards/social-studies/world-history/era-2-middle-ages.md | PENDING |
| Cross-link Era 3 | docs/standards/social-studies/world-history/era-3-revolutions.md | PENDING |
| Cross-link Era 4 | docs/standards/social-studies/world-history/era-4-global-war.md | PENDING |
| Cross-link USH Unit 1 | docs/standards/social-studies/us-history/unit-1-industrial.md | PENDING |
| Cross-link USH Unit 2 | docs/standards/social-studies/us-history/unit-2-imperialism-wwi.md | PENDING |
| Cross-link USH Unit 3 | docs/standards/social-studies/us-history/unit-3-roaring-20s.md | PENDING |
| Cross-link USH Unit 4 | docs/standards/social-studies/us-history/unit-4-wwii.md | PENDING |
| Cross-link USH Unit 5 | docs/standards/social-studies/us-history/unit-5-cold-war.md | PENDING |
| Cross-link USH Unit 6 | docs/standards/social-studies/us-history/unit-6-civil-rights.md | PENDING |
| Cross-link USH Unit 7 | docs/standards/social-studies/us-history/unit-7-vietnam.md | PENDING |
| Cross-link USH Unit 8 | docs/standards/social-studies/us-history/unit-8-1970s-1980s.md | PENDING |
| Cross-link USH Unit 9 | docs/standards/social-studies/us-history/unit-9-1990s-2000s.md | PENDING |

Reference: era-1-civilizations.md (lines 235–267) is the template. Match that structure.

---

## PRIORITY 2 — Skinny Batch Generation (World History)

Generate all remaining WH skinnies. Each standard × 4 eras = 24 skinnies total.
Ones already done are marked DONE. Use the skinny-template.md as the base.
Save to: `docs/skinnies/world-history/era-[N]/[wh-standard]-[slug]-skinny.md`

Naming convention: `wh-6-12-[N]-[topic-slug]-skinny.md`

| Skinny | File | Status |
|--------|------|--------|
| WH.6_12.2 + Era 1 (Belief Systems) | docs/skinnies/world-history/era-1/wh-6-12-2-belief-systems-skinny.md | DONE |
| WH.6_12.3 + Era 1 (Political Systems) | docs/skinnies/world-history/era-1/wh-6-12-3-political-systems-era1-skinny.md | DONE |
| WH.6_12.3 + Era 2 (Medieval Political) | docs/skinnies/world-history/era-2/wh-6-12-3-medieval-political-skinny.md | DONE |
| WH.6_12.4 + Era 3 (Revolution Social/Economic) | docs/skinnies/world-history/era-3/wh-6-12-4-revolution-social-economic-skinny.md | DONE |
| WH.6_12.1 + Era 1 (Science & Tech) | docs/skinnies/world-history/era-1/wh-6-12-1-science-tech-era1-skinny.md | PENDING |
| WH.6_12.4 + Era 1 (Social/Economic) | docs/skinnies/world-history/era-1/wh-6-12-4-social-economic-era1-skinny.md | PENDING |
| WH.6_12.5 + Era 1 (Cause & Effect) | docs/skinnies/world-history/era-1/wh-6-12-5-cause-effect-era1-skinny.md | PENDING |
| WH.6_12.6 + Era 1 (Past to Present) | docs/skinnies/world-history/era-1/wh-6-12-6-past-present-era1-skinny.md | PENDING |
| WH.6_12.1 + Era 2 (Medieval Science/Tech) | docs/skinnies/world-history/era-2/wh-6-12-1-science-tech-era2-skinny.md | PENDING |
| WH.6_12.2 + Era 2 (Medieval Religion) | docs/skinnies/world-history/era-2/wh-6-12-2-religion-era2-skinny.md | PENDING |
| WH.6_12.4 + Era 2 (Medieval Social) | docs/skinnies/world-history/era-2/wh-6-12-4-social-era2-skinny.md | PENDING |
| WH.6_12.5 + Era 2 (Medieval Cause/Effect) | docs/skinnies/world-history/era-2/wh-6-12-5-cause-effect-era2-skinny.md | PENDING |
| WH.6_12.6 + Era 2 (Medieval to Present) | docs/skinnies/world-history/era-2/wh-6-12-6-past-present-era2-skinny.md | PENDING |
| WH.6_12.1 + Era 3 (Revolution Science/Tech) | docs/skinnies/world-history/era-3/wh-6-12-1-science-tech-era3-skinny.md | PENDING |
| WH.6_12.2 + Era 3 (Revolution Religion/Ideology) | docs/skinnies/world-history/era-3/wh-6-12-2-ideology-era3-skinny.md | PENDING |
| WH.6_12.3 + Era 3 (Revolution Political) | docs/skinnies/world-history/era-3/wh-6-12-3-political-era3-skinny.md | PENDING |
| WH.6_12.5 + Era 3 (Revolution Cause/Effect) | docs/skinnies/world-history/era-3/wh-6-12-5-cause-effect-era3-skinny.md | PENDING |
| WH.6_12.6 + Era 3 (Revolution to Present) | docs/skinnies/world-history/era-3/wh-6-12-6-past-present-era3-skinny.md | PENDING |
| WH.6_12.1 + Era 4 (20th-C Science/Tech) | docs/skinnies/world-history/era-4/wh-6-12-1-science-tech-era4-skinny.md | PENDING |
| WH.6_12.2 + Era 4 (20th-C Ideology) | docs/skinnies/world-history/era-4/wh-6-12-2-ideology-era4-skinny.md | PENDING |
| WH.6_12.3 + Era 4 (20th-C Political) | docs/skinnies/world-history/era-4/wh-6-12-3-political-era4-skinny.md | PENDING |
| WH.6_12.4 + Era 4 (20th-C Social) | docs/skinnies/world-history/era-4/wh-6-12-4-social-era4-skinny.md | PENDING |
| WH.6_12.5 + Era 4 (20th-C Cause/Effect) | docs/skinnies/world-history/era-4/wh-6-12-5-cause-effect-era4-skinny.md | PENDING |
| WH.6_12.6 + Era 4 (Past to Present) | docs/skinnies/world-history/era-4/wh-6-12-6-past-present-era4-skinny.md | PENDING |

---

## PRIORITY 3 — Skinny Batch Generation (ELA 9-10)

Generate ELA skinnies for active standards. 1 skinny per standard = 12 skinnies.
Save to: `docs/skinnies/ela9/` or `docs/skinnies/ela10/`
Naming convention: `[standard-code]-[topic-slug]-skinny.md` (e.g., `r9-informational-argumentative-skinny.md`)

| Skinny | File | Status |
|--------|------|--------|
| 9-10.R.2 (Comprehension/Inference) | docs/skinnies/ela9/r2-comprehension-inference-skinny.md | PENDING |
| 9-10.R.4 (Main Idea/Theme) | docs/skinnies/ela9/r4-main-idea-theme-skinny.md | PENDING |
| 9-10.R.7 (Style/Word Choice) | docs/skinnies/ela9/r7-style-word-choice-skinny.md | PENDING |
| 9-10.R.8 (Literary Elements) | docs/skinnies/ela9/r8-literary-elements-skinny.md | PENDING |
| 9-10.R.9 (Informational/Argumentative) | docs/skinnies/ela9/r9-informational-argumentative-skinny.md | PENDING |
| 9-10.W.3 (Explanatory Writing) | docs/skinnies/ela9/w3-explanatory-writing-skinny.md | PENDING |
| 9-10.W.4 (Argument Writing) | docs/skinnies/ela9/w4-argument-writing-skinny.md | PENDING |
| 9-10.W.6 (Writing Process) | docs/skinnies/ela9/w6-writing-process-skinny.md | PENDING |
| 9-10.C.1 (Formal Presentation) | docs/skinnies/ela9/c1-formal-presentation-skinny.md | PENDING |
| 9-10.C.6 (Discussion/Debate) | docs/skinnies/ela9/c6-discussion-debate-skinny.md | PENDING |
| 9-10.IR.1–5 (Research Bundle) | docs/skinnies/ela9/ir1-5-research-bundle-skinny.md | PENDING |
| 9-10.L.1 (Language/Usage) | docs/skinnies/ela9/l1-language-usage-skinny.md | PENDING |

---

## PRIORITY 4 — Reading Library Ingest Queue

Process these texts from public domain sources into full reading library entries.
For Project Gutenberg texts: fetch from gutenberg.org, process directly.
See AGENTS.md → Library Curator for the entry format.

| Text | Source | Target | Status |
|------|--------|--------|--------|
| Analects of Confucius | gutenberg.org/ebooks/4094 | docs/reading-library/social-studies/analects-confucius.md | PENDING |
| Book of the Dead (Egypt) — selections | public domain | docs/reading-library/social-studies/book-of-the-dead-egypt.md | PENDING |
| Communist Manifesto — selections | gutenberg.org/ebooks/61 | docs/reading-library/social-studies/communist-manifesto.md | PENDING |
| Haitian Declaration of Independence | thelouvertureproject.org | docs/reading-library/social-studies/haitian-declaration.md | PENDING |
| UN Declaration of Human Rights | un.org/en/about-us/universal-declaration-of-human-rights | docs/reading-library/social-studies/un-declaration-human-rights.md | PENDING |
| Narrative of Frederick Douglass | gutenberg.org/ebooks/23 | docs/reading-library/social-studies/narrative-douglass.md | PENDING |
| The Jungle — Sinclair (selections) | gutenberg.org/ebooks/140 | docs/reading-library/ela/jungle-sinclair.md | PENDING |
| FDR Four Freedoms Speech | archives.gov | docs/reading-library/social-studies/fdr-four-freedoms.md | PENDING |

---

## PRIORITY 5 — MkDocs Setup & Serving on T480

These are one-time setup tasks for getting the wiki running on hermespad.

| Task | Status |
|------|--------|
| Install mkdocs + mkdocs-material: `pip install mkdocs mkdocs-material` | DONE |
| Install mkdocs plugins: `pip install mkdocs-awesome-pages-plugin` | DONE |
| Test serve: `cd ~/Desktop/sda-wiki && mkdocs serve -a 0.0.0.0:5010` | DONE |
| Verify wiki renders at http://hermespad:5010 | DONE |
| Create systemd service for mkdocs (auto-start on boot) | DONE |
| Fix mkdocs.yml nav mismatches (unit-2, unit-3, unit-8 file names) | PENDING |

mkdocs.yml nav currently expects these names — actual files have different names:
- Expected: unit-2-progressive.md — Actual: unit-2-imperialism-wwi.md
- Expected: unit-3-wwi-interwar.md — Actual: unit-3-roaring-20s.md
- Expected: unit-8-reagan.md — Actual: unit-8-1970s-1980s.md

Fix: update mkdocs.yml nav section to match actual file names.

---

## PRIORITY 6 — US History Skinny Batch

After WH and ELA skinnies are done. Same structure.
6 standards × 9 units = 54 skinnies. Generate in unit order.
Save to: `docs/skinnies/us-history/unit-[N]/`

Status: PENDING (do not start until WH + ELA skinnies are complete)

---

## COMPLETED

| Task | Date | Notes |
|------|------|-------|
| All 8 reading library entries with real hyperlinks | 2026-06-10 | hammurabi, magna-carta, common-sense, declaration-rights-man, wollstonecraft, mlk-letter, night-wiesel, orwell-1984 |
| Wikilink bracket conversion (53 files) | 2026-06-10 | All [[...]] → [Label](path.md) |
| Era 1 cross-linking | 2026-06-10 | Skinnies, reading library, crashcourse, ELA standards sections added |
| Resource Bank pages | 2026-06-10 | resources/index.md, primary-sources/index.md, fps-framers/index.md, ingest.md |
| 4 existing skinnies | 2026-06-10 | WH.6_12.2 Era1, WH.6_12.3 Era1, WH.6_12.3 Era2, WH.6_12.4 Era3 |
| SDA theme CSS (matching phil_wiki) | 2026-06-10 | Playfair Display throughout, dark green/gold scheme |
| All standards pages (WH 4 eras + USH 9 units) | 2026-06-10 | Full content with standards, learning targets, inquiry angles |
| mkdocs.yml with full navigation | 2026-06-10 | All sections configured |

---

*Hermes Work Queue · SDA Commons Wiki · Updated 2026-06-10*
*Read AGENTS.md for full program context and skill specs.*
