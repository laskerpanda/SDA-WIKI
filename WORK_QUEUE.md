# SDA Wiki — Hermes Work Queue
# Last updated: 2026-06-24
# Purpose: Hermes reads this file to know what to build next.
# Update status inline as you work. Commit after every completed item.

---

## HOW TO USE THIS FILE

Pick the highest-priority PENDING item. Do it. Change its status to DONE. Commit. Move to the next.
If you're blocked, mark BLOCKED and add a note. Notify Reese via Telegram.

Hermes: read this file at the start of every wiki session before doing any other wiki work.

---

## CURRENT STATUS — June 24, 2026

**Wiki is functionally complete for Year 1 (Grade 9).** All WH skinnies, ELA skinnies, reading library, and studio packets are done. Remaining work is cross-linking (navigation convenience), pre-school cleanup (before August 2026), and USH skinnies (Grade 10 / Year 2 — hold until October 2026).

---

## PRIORITY 0 — Pre-School Cleanup (Before August 20, 2026)

These tasks must be complete before students access any wiki materials. Claude Code handles all of these — Hermes does not touch sda-wiki directly.

| Task | Details | Status |
|------|---------|--------|
| Audit student-visible pages | Review all pages in `sda-wiki-site/` that students might access. Confirm no teacher-facing operational notes, Hermes agent references, or build system details appear in student-visible output. | PENDING |
| Review `docs/AGENTS.md` visibility | AGENTS.md is the agent spec — it should NOT appear in the sda-wiki-site student build. Confirm mkdocs.yml excludes it from the nav, or move to a teacher-only location. | PENDING |
| Review `WORK_QUEUE.md` visibility | This file is operational. Confirm it is excluded from sda-wiki-site build. | PENDING |
| Review `REVIEW_LOG.md` visibility | Confirm it is excluded from sda-wiki-site build. | PENDING |
| Confirm `_Hermes — Workshop/` is not published | This folder must never appear in any published or student-accessible output. | PENDING |
| Strip teacher-facing language from student pages | Any page in `2026-27 — For Students/` that references Hermes, Claude Code, build scripts, or teacher workflow should have that language removed before school. | PENDING |
| Final audit of `2026-27 — For Students/` | Reese reviews all student-facing studio packets for accuracy, tone, and appropriateness before August. | PENDING — Reese reviews |

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

## PRIORITY 2 — CrashCourse Expansion (Ongoing)

5 entries currently exist. Add ~15 more for WH eras and USH units.
Each entry: episode link, 3 key timestamps with content notes, watch prompt for annotation, standards connection.

**WH priorities:**
- Agricultural Revolution, Silk Road, Feudalism, The Crusades, The Renaissance, Scientific Revolution, French Revolution, Imperialism, WWI, WWII, Cold War

**USH priorities:**
- Industrial Revolution, Progressive Era, WWI, Great Depression, WWII, Civil Rights, Vietnam

| Task | Status |
|------|--------|
| WH CrashCourse expansion (11 episodes) | PENDING |
| USH CrashCourse expansion (7 episodes) | PENDING |

---

## PRIORITY 3 — USH Skinny Batch (Grade 10 / Year 2)

54 skinnies: 6 standards × 9 units. Grade 10 uses USH starting Year 2.
**Do not start until October 2026** — not needed before first-year school starts.

Save to: `docs/skinnies/us-history/unit-[N]/`
Naming: `us-6-12-[standard]-[slug]-unit[N]-skinny.md`

**Suggested order:** Units 1–4 before December 2026, Units 5–9 by March 2027.

Status: PENDING — do not start until October 2026

---

## COMPLETED — All Phase 1–5 Work (June 10–12, 2026)

| Task | Date | Notes |
|------|------|-------|
| Wiki skeleton and folder structure | 2026-06-10 | All directories created per AGENTS.md spec |
| All 15 standards pages (WH × 4 eras, USH × 9 units, ELA) | 2026-06-10 | Full content |
| mkdocs.yml nav fixes (unit-2, unit-3, unit-8 filenames) | 2026-06-10 | ✅ fixed |
| SDA theme CSS (dark green/gold, matching phil_wiki) | 2026-06-10 | |
| All standards pages cross-linking (Era 1 done as template) | 2026-06-10 | Pattern at era-1-civilizations.md:235–267 |
| Wikilink bracket conversion (53 files) | 2026-06-10 | All [[...]] → [Label](path.md) |
| Student guide (How to SDA) | 2026-06-10 | Full lifecycle, ownership levels, portfolio defense |
| Skinny template | 2026-06-10 | Full anatomy, all 6 demo modes |
| Resource Bank pages | 2026-06-10 | resources/index.md, primary-sources/index.md, fps-framers/index.md, ingest.md |
| **WH Skinnies — All 24** | 2026-06-11 | 6 standards × 4 eras; all in docs/skinnies/world-history/ |
| **ELA Skinnies — All 12** | 2026-06-11 | R.2, R.4, R.7, R.8, R.9, W.3, W.4, W.6, C.1, C.6, IR.1-5, L.1 |
| **Reading Library — 28+ entries** | 2026-06-11–12 | 22 social studies + 8 ELA dual-use; exceeded original 16-entry target |
| **Studio Packets — All 8** | 2026-06-12 | WH-01 through WH-06 + USH-01 + USH-02; full six-week arcs |
| Studio archive index | 2026-06-12 | docs/units/studio-archive/index.md with sequencing guide |
| Reading library index | 2026-06-12 | docs/reading-library/index.md with full linked tables by era |

---

## STUDIO PACKETS BUILT — Quick Reference

| Code | File | Essential Question |
|------|------|-------------------|
| WH-01 | docs/units/studio-archive/wh-01-who-should-govern.md | Who should govern, and what gives them the right? |
| WH-02 | docs/units/studio-archive/wh-02-rights-chain.md | When people write down their rights, what changes — and what doesn't? |
| WH-03 | docs/units/studio-archive/wh-03-writing-against-empire.md | When a powerful system is doing harm, what does it take to challenge it? |
| WH-04 | docs/units/studio-archive/wh-04-reformation-and-revolution.md | Can one document change the world — and if so, how? |
| WH-05 | docs/units/studio-archive/wh-05-the-cost-of-war.md | Who pays the cost of war — and who gets to tell the story? |
| WH-06 | docs/units/studio-archive/wh-06-connected-world.md | What connects the world — and who decides who counts as part of it? |
| USH-01 | docs/units/studio-archive/ush-01-when-the-system-fails.md | When an institution fails the people it's supposed to serve, what does it take to fix it? |
| USH-02 | docs/units/studio-archive/ush-02-literature-of-fear.md | What does a society's fiction reveal about its fears — and whose fears count? |

---

## READING LIBRARY — COMPLETE INVENTORY

### Social Studies (22 entries)
**Era 1:** Hammurabi's Code · Analects of Confucius · Pericles' Funeral Oration · Melian Dialogue
**Era 2:** Magna Carta · Ibn Battuta Rihla · Luther 95 Theses · Las Casas Short Account
**Era 3:** Common Sense · Declaration of Rights of Man · Wollstonecraft Vindication · Haitian Declaration · Communist Manifesto · Narrative of Douglass · Kipling + H.T. Johnson · The Jungle · Dulce et Decorum Est
**Era 4 / USH:** MLK Letter · FDR Four Freedoms · UN UDHR · Mandela Rivonia Speech · Malala UN Speech

### ELA Dual-Use (8 entries)
Julius Caesar · Night (Wiesel) · Fahrenheit 451 · 1984 · Warriors Don't Cry · Persepolis · (+ Hammurabi and Jungle also serve as dual-use)

---

*Hermes Work Queue · SDA Commons Wiki · Updated 2026-06-12*
*Read AGENTS.md for full program context and skill specs.*
