# Before August — Setup Checklist

!!! warning "Remove this tab before school starts"
    This page is a temporary pre-launch checklist for Mr. Reese. Once every item is checked off, remove the "Before August" section from `mkdocs.yml` and rebuild. Instructions at the bottom of this page.

---

Everything on this page needs to happen before students arrive. Items are sorted by urgency — **Section 1 is the hard blocker**, nothing else matters until those are done.

---

## Section 1 — Must Have Before Day 1

These items directly affect what students can do on the first day of school.

---

### ☑ 1. Upload Student Tracker Templates to Google Drive — COMPLETE (June 21, 2026)

Trackers uploaded to Google Drive and wired into `docs/commons/standards-tracker.md` with `/copy` links. Students click → Google prompts "Make a Copy" automatically.

- Grade 9 Tracker: `docs.google.com/spreadsheets/d/1nX_1lJ9AVUDHgeO8ZGOGJFHdJynnLRhz/copy`
- Grade 10 Tracker: `docs.google.com/spreadsheets/d/1Zkzxq7DvwdFQ_dMmbPsyIz6o8ykAYdY3/copy`

---

### ☑ 2. Add Real Google Doc Links — Studio Contract, Source Log, Reflection — COMPLETE (June 21, 2026)

All 6 placeholder links replaced in `docs/commons/student-workflow.md`. All three docs wired with `/copy` links. Also appears in the quick-reference table at the bottom of the page.

- Studio Contract: `docs.google.com/document/d/16IfJOUHWeECuPQ3FA6bmEoRNHZgks_YW/copy`
- Source Log: `docs.google.com/document/d/1Q0OFqHVgAFfb0e8wjURTxO0nYFedBkVa/copy`
- Reflection: `docs.google.com/document/d/1dchL1IuG-orMxJnhCsZyTUwC3swuzTy7/copy`

---

### ☐ 3. Define How Studio Scores Map to Grades (Infinite Campus)

The FAQ (`docs/commons/faq.md`) says scores go into Infinite Campus at semester end, but the *mapping* is not defined anywhere in the wiki. Students and parents will ask.

**Questions to answer:**
- Does 3.0 = an A? B? Proficient = passing?
- Are all standards weighted equally in the gradebook?
- Is the semester grade the average of all studio scores, or the highest score per standard?
- What happens to standards that were never targeted (student chose different studios)?

**Once decided:** Add a "How Grading Works" section to `docs/commons/faq.md` and `docs/commons/how-to-sda/index.md`.

---

### ☐ 4. Decide Which Studio Runs First

**Grade 9:** WH-01 "Who Should Govern?" assumed for September.
**Grade 10:** USH-01 "When an Institution Fails" assumed for September.

Confirm or change. No wiki edit needed — just the decision.

---

### ☐ 5. Set Up Student Google Drive Folders

Students need their personal folder in The Commons before they can file anything.

**Folder structure per student:**
```
The Commons
  └── Grade 9 ELA / World History  (or Grade 10 ELA / US History)
        └── [Last Name, First Name]
              ├── Studio Contracts
              ├── Standards Tracker     ← copy of the template from Item 1
              ├── Studio Journal        ← one Google Doc, new entry added each Friday
              └── [Studio folders — created as they go]
```

**Option:** Have students create their own folder structure on Day 1 with the template above on the board. Five minutes, no pre-work for you.

**For the Studio Journal:** Students create one Google Doc inside their Studio Journal folder on Day 1 and title it `Studio Journal — [Last Name, First Name]`. They add a new entry every Friday at the top (newest first). No template to upload — they copy the three-line format from the [Studio Journal wiki page](../commons/studio-journal.md).

---

### ☐ 6. Configure Headrush

Headrush is the platform where Demo scores are formally recorded and eventually bridge to Infinite Campus.

**Minimum needed before Day 1:**
- Student roster imported
- Projects created for ELA standards + first SS standards (at minimum)
- 1.0 / 2.0 / 3.0 / 4.0 scale configured to match SDA rubric
- Students know how to log in

**Once configured:** Update `docs/build-a-studio/when-youre-done.md` → Step 6 (Headrush section) with the real project name and submission instructions.

---

### ☐ 7. Decide the sda_webapp Status

Flask app lives at `thelastmorphy:5002`. Status unknown.

**Decision needed:** Is this app required before Day 1, or can it stay dark?
- If yes: verify it runs, confirm what it does, document it
- If no: note it as deferred in the completion plan (already done)

---

## Section 2 — Must Have Before Quarter 1 Expo

---

### ☐ 8. Set Exhibition Dates — All Four Expos

Plan: 4 expos per year, one per quarter.

**Dates to set:**
- Q1 Expo — Fall
- Q2 Expo — Winter
- Q3 Expo — Spring
- Q4 Expo — End of Year / Portfolio Defense

**Once set:** Add exact dates to `docs/commons/exhibition-prep.md` and `docs/commons/student-workflow.md`.

---

### ☐ 9. Define the Portfolio Defense Format

A portfolio defense page is planned but not written — the format has to come first.

**Questions to answer:**
- Is the Q4 Expo the portfolio defense, or a separate event?
- What does a student present? (Best studio? Growth across all studios? Standard coverage?)
- Who is the audience? (Mr. Reese only / peers / parents / outside panel?)
- Is it scored, and on what rubric?

**Once defined:** Write `docs/commons/portfolio-defense.md`.

---

### ☑ 10a. Deploy Wiki — Phase 1 GitHub Pages COMPLETE (June 21, 2026) · ☐ 10b. Phase 2 Cloudflare Access — PENDING

**Phase 1 done:** Wiki live at `https://laskerpanda.github.io/SDA-WIKI/` · GitHub Actions auto-deploy on every push · SSH key on GitHub · repo public for principal meeting June 22 → make private after.

**Phase 2 still needed before school:** Buy domain → Cloudflare Pages → Cloudflare Access with @fargoschools.org Google OAuth. See instructions below.

**Decision made:** Cloudflare Pages + Cloudflare Access (Google OAuth restricted to @fargoschools.org). Two-phase rollout:

---

**Phase 1 — GitHub Pages (do this now — needed for principal demo + required for Phase 2)**

The git repo is already initialized in `sda-wiki/`. You need to push it to GitHub.

1. Create a free account at github.com if you don't have one
2. Create a new **private** repository — suggested name: `sda-wiki`
3. On Hermes, open a terminal and run:

```bash
cd ~/Desktop/SDA\ COMMONS/_System\ —\ Wiki\ \&\ Build/sda-wiki
git remote add origin https://github.com/YOUR-USERNAME/sda-wiki.git
git add -A
git commit -m "June 2026 — full wiki build"
git branch -M main
git push -u origin main
```

4. In GitHub: Settings → Pages → Source: **Deploy from branch** → Branch: `gh-pages` → Save
5. Back on Hermes, deploy:

```bash
cd ~/Desktop/SDA\ COMMONS/_System\ —\ Wiki\ \&\ Build/sda-wiki
mkdocs gh-deploy
```

Your principal can access the wiki at: `https://YOUR-USERNAME.github.io/sda-wiki/`

**Note:** GitHub Pages is public by default — anyone with the URL can read it. That's fine for the principal demo. Auth is added in Phase 2.

!!! warning "After the principal meeting"
    Make the repo private again: **github.com/laskerpanda/SDA-WIKI/settings** → Danger Zone → Change visibility → Private. GitHub Pages will stop serving until Phase 2 (Cloudflare) is set up.

---

**Phase 2 — Cloudflare Access (before school starts — adds Google login for students)**

Prerequisites: a domain name (~$10/yr at cloudflare.com/products/registrar).

1. Buy a domain via Cloudflare Registrar (e.g. `sdacommons.org`)
2. In Cloudflare: Pages → Connect to GitHub → select `sda-wiki` repo → build command `mkdocs build` → output `site`
3. In Cloudflare Zero Trust → Access → Applications → add your domain
4. Identity provider: Google → restrict email domain to `@fargoschools.org`
5. Students visit `sdacommons.org`, log in with school Google account, done

**Cost:** Cloudflare free tier covers up to 50 users. Domain ~$10/yr. Everything else is free.

---

## Section 3 — Content To Add (Can Wait Until After School Starts)

These are real gaps in the wiki content. None block Day 1, but students will notice them within the first month.

---

### ☑ 11. CrashCourse YouTube Links — COMPLETE (June 21, 2026)

Audited and fixed all CrashCourse YouTube links across 40 pages.

| Status | Count | What |
|--------|-------|------|
| ✓ Confirmed + linked | 34 | All WH (20 pages) + all USH (7 pages) + 13 of 19 Literature pages |
| ✗ No official CC episode | 6 | Julius Caesar, Moby Dick, Fahrenheit 451, Raisin in the Sun, Caged Bird Sings, Kite Runner |

**No official CrashCourse episodes exist** for those 6 books — they keep their "Search YouTube" placeholder. These are niche titles that CrashCourse hasn't covered. If you want video support for these, look for TED-Ed or Khan Academy alternatives.

**WH sources:** Original CC WH series (PLBDA2E52FB1EF80C9) + CC European History for Reformation, Enlightenment, Napoleon, Industrial Revolution, WWII Part 2, Black Death.

**Transcripts:** 52 of 59 CC pages have "Transcript pending." Pull on-demand as episodes are assigned — start with whichever episode goes first in Studio 1.

---

### ☑ 12. CrashCourse WH Episodes — COMPLETE (June 21, 2026)

All 27 CrashCourse World History episode pages are now built. All skinny "coming soon" links have been corrected and wired to real episode pages. Episode numbers that were wrong in the original skinnies have been fixed.

**Coverage:** Eps 01, 03, 08, 09, 12, 13, 14, 15, 17, 22, 23, 24, 25, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42 — all nav entries in order.

---

### ☐ 13. Reading Library Content Gaps

Two specific gaps flagged in the wiki:

**Elie Wiesel Nobel Prize Speech (1986)**
Referenced in the WH Era 4 / WH.6 skinny as "coming soon." Strong pairing with *Night*. Public domain — can be added as a reading library entry.
File would go: `reading-library/social-studies/wiesel-nobel-speech.md`

**Vietnam-Era Primary Sources**
Referenced in `crosswalk/gr10/units-7-9.md` as "not yet in the reading library." Strong candidates: Pentagon Papers excerpts, MLK's "Beyond Vietnam" speech (1967), anti-war protest documents.
These would go in `reading-library/social-studies/` — Era 4 / USH Unit 7.

**What to do:** Hermes can build these entries when you're ready. No blockers.

---

### ☑ 14. Teacher Guide — COMPLETE (June 21, 2026)

Built and saved at: `2026-27 — For Teachers/Program Overview/teacher-guide-2026-27.html`

Covers: Year arc & pacing · Studio launch protocol · Contract approval guide · Scoring guide · Crosswalk requirements · Red flag indicators · Exhibition logistics · Headrush → IC workflow · Google Drive management · Parent communication templates (3 ready-to-send email drafts).

---

## Section 4 — Deferred (After School Starts, When Wiki Is Stable)

| Item | Notes |
|------|-------|
| CrashCourse transcripts | Pull on-demand as episodes are assigned (see Item 11) |
| Reading Library ingest system | Future project — design decisions needed first |
| Hermes Kanban | Implement after Hermes is reliable |

---

## Section 5 — Phase 2 Development (Planned, Not Started)

These are the next build priorities after the core wiki is stable. They deepen the student experience and move toward a fully integrated classroom environment.

---

### ☑ 15. Studio Packet HTML Documents — COMPLETE

All 13 studio packet HTML documents are built and saved in `2026-27 — For Students/Studio Packets/`. Potions Master aesthetic, 6-week arc, standards, suggested sources, thought card prompts. All 13 studio wiki pages also have era timeline SVG diagrams embedded.

---

### ☑ 16. Wiki Content Map — COMPLETE (June 2026)

Live at `localhost:5010/content-map.html`. D3.js force-directed graph, 67 nodes, 13 studios, all connections. Node types: WH Studios (amber) · USH Studios (green) · ELA Standards · WH/USH Standards · Primary Sources · Literary Texts · CrashCourse Hubs. Click any node to open the corresponding wiki page. Legend filters by node type. CrashCourse hub nodes show episode counts.

---

### ☑ 17. Images for Content Pages — COMPLETE (June 21, 2026)

**Reading library:** 26 entries now have embedded Wikimedia Commons portrait/artifact images (author portraits, manuscript scans, historical artifacts). Images load client-side from Wikimedia — no local storage needed.

**Studio wiki pages:** All 13 studio pages have era timeline SVG diagrams showing which historical period the studio covers (amber = WH, green = USH). Self-generated, no external dependencies.

---

### ☐ 18. Studio Packet Pages — Thought Card Integration

Each studio packet page in the wiki should explicitly surface relevant thought card prompts in a "When You're Stuck" callout — pulling the 3–4 most applicable questions from classroom-cards.html for that studio's essential question and standards.

This connects the physical classroom cards (posted on walls) to the digital wiki, so students see the same cognitive scaffolding in both places.

---

## When You're Done — Remove This Tab

**Step 1:** Open `sda-wiki/mkdocs.yml`

**Step 2:** Delete these lines from the `nav:` section:
```yaml
  - Before August:
    - Checklist: before-august/index.md
```

**Step 3:** Rebuild and restart:
```bash
cd ~/Desktop/SDA\ COMMONS/_System\ —\ Wiki\ \&\ Build/sda-wiki
mkdocs build
systemctl --user restart sda-wiki.service
```

The `docs/before-august/` folder can stay on disk — it just won't appear in the nav.

---

*Before August Checklist · SDA Commons Wiki — Internal Use Only*
*This tab is not student-facing. Remove from nav before school starts.*
