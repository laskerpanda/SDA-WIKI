#!/usr/bin/env python3
"""Generate 8 skinnies for SDA Commons Wiki using gemma4:12b via Ollama."""

import requests
import json
import os
import time

SYSTEM_PROMPT = """You are writing a "skinny" — a focused mini-lesson for 9th and 10th grade students in the Self-Directed Academy at South High School, Fargo ND. The SDA is a mastery-based project learning program integrating English and Social Studies. Students are motivated and capable. Write bottom-up (define terms before using them), example-first, no jargon without definition. The NDSBL proficiency scale is 1.0/1.5/2.0/2.5/3.0/3.5/4.0. A 3.0 means meeting the standard — no major errors. A 4.0 means going beyond. A 2.0 means you know the basics but struggle with complexity. The skinny must include all six demonstration of learning modes. Use ## headings, tables for the demo modes, and specific concrete examples. Output clean markdown."""

def generate(prompt, system=SYSTEM_PROMPT, model="gemma4:12b"):
    for attempt in range(2):
        try:
            r = requests.post("http://localhost:11434/api/generate", json={
                "model": model,
                "prompt": prompt,
                "system": system,
                "stream": False,
                "options": {"num_ctx": 8192, "temperature": 0.3}
            }, timeout=300)
            r.raise_for_status()
            return r.json()["response"]
        except Exception as e:
            print(f"  Attempt {attempt+1} failed: {e}")
            if attempt == 0:
                print("  Retrying with shorter prompt...")
                prompt = prompt[:2000]
            else:
                raise

SKINNIES = [
    {
        "id": 1,
        "path": "/home/thinkstation/sda-wiki/skinnies/world-history/era-1/wh-6-12-2-belief-systems-skinny.md",
        "prompt": """Write a complete SDA skinny mini-lesson in clean markdown following this EXACT structure:

# How Early Belief Systems Shaped Civilization — Skinny

**Standard:** WH.6_12.2 — Explain historical changes related to religions and ideologies
**Era/Unit (if SS):** Era 1 — Emergence of Civilizations and Religions Around the Globe
**ELA Crosswalk:** 9-10.R.9 — Analyze informational/argumentative elements, author POV and bias
**NDSBL Target:** 3.0 score
**Estimated Time:** 60–90 minutes
**Subject:** World History + ELA crosswalk

---

## What You Need to Know (Score 2.0)

[Write a plain-language foundation section. Define ALL of the following terms with clear student-readable definitions:
- Belief system
- Monotheism
- Polytheism
- Ideology
- Primary source
- Code of law (with Hammurabi example)
- Dharma (Hindu concept)
- The Four Noble Truths (Buddhism)
- Afterlife / Ka (Egyptian concept)

Then list 5 basic processes students should be able to do (as checkboxes).
End with a concrete 2.0 example: "A student who can..." — specific to this content.]

---

## The Standard (Score 3.0)

**WH.6_12.2 — Explain historical changes related to religions and ideologies**

[Write the full 3.0 section. Include:
- What meeting the standard means in plain language
- A specific, concrete 3.0 example focused on analyzing how Hammurabi's Code, Egyptian religious texts (Book of the Dead), or early Hindu/Buddhist writings show how belief systems shaped political power, social order, and daily life
- One clear sentence distinguishing 3.0 from 2.0]

---

## Going Further (Score 4.0)

[Write 3 specific transfer tasks connecting belief systems across eras or comparing multiple civilizations. Include one concrete 4.0 example.]

---

## CrashCourse Connection

**Video:** Mesopotamia: Crash Course World History #3 — https://www.youtube.com/watch?v=sohXPx_XZ6Y
**Also:** The Indus Valley Civilization — https://www.youtube.com/watch?v=n7ndRwqJYDM

**Key Timestamps:**
- [Write 3 specific timestamps with what happens and why it matters for this standard — make them realistic and content-accurate for Mesopotamia/early civilizations CrashCourse episodes]

**Watch Prompt:** As you watch, track: [write a specific annotation task]

---

## Reading Library Connection

- [[reading-library/social-studies/hammurabis-code]] — [one sentence on connection to WH.6_12.2]
- [[reading-library/social-studies/book-of-the-dead-egypt]] — [one sentence]
- [[reading-library/social-studies/dhammapada-buddhism]] — [one sentence]

---

## Demonstration of Learning — Choose One

**How will you show you know this standard?** Pick one mode.

| # | Mode | What You Do for This Specific Standard |
|---|------|----------------------------------------|
| 1 | **Written Assessment** | [Write a specific prompt about how one primary source (Hammurabi's Code OR Egyptian Book of the Dead OR early Buddhist texts) reveals how that civilization's beliefs shaped its political or social structure. The prompt must target WH.6_12.2 specifically.] |
| 2 | **Extended Writing** | [Write a specific 400-600 word essay prompt requiring the student to explain how TWO early civilizations' belief systems shaped their laws or social structure — using specific evidence from primary sources] |
| 3 | **Verbal Conversation** | [Write what the student must be able to talk through: 3 specific things they should explain verbally about early belief systems and their political/social effects] |
| 4 | **Visual/Creative** | [Write a specific sketchnote/diagram task — what elements it must include to demonstrate WH.6_12.2] |
| 5 | **Multimedia/Performance** | [Write a specific podcast or video task — what it must cover about early belief systems] |
| 6 | **Portfolio Annotation** | [Write the portfolio annotation task — what existing work to select and what metacognitive connection to make, using 2.0/3.0/4.0 language] |

---

## Deliverable Ideas (Your Studio Product)

**These are NOT the demonstration of learning.** These are PBL artifact ideas.

1. **[Title]** — [Specific deliverable description with format, audience, and real-world purpose]
2. **[Title]** — [Second deliverable idea — different format/audience]
3. **[Title]** — [Third deliverable idea]

---

## Scale Tasks

- [ ] **2.0 task:** [Concrete, completable task a student can independently check off — identify something specific in Hammurabi's Code or another primary source]
- [ ] **3.0 task:** [Standard-demonstrating task — matches WH.6_12.2 language — analyze how a specific belief system shaped political/social life, with evidence]
- [ ] **4.0 task:** [Extension/synthesis task — compare belief systems across two civilizations or connect to a present-day ideology]

---

## See Also

- [[standards/social-studies/world-history/era-1-civilizations]] — Era 1 overview
- [[standards/social-studies/world-history/standards-overview#WH.6_12.2]] — full standard with all era applications
- [[standards/ela/gr9-10-scales#9-10.R.9]] — R.9 crosswalk (analyzing informational texts, author POV)
- [[skinnies/ela9/r9-informational-argumentative-skinny]] — R.9 skinny
- [[skinnies/templates/research-skinny]] — IR.1–IR.5 research skills

---

**How to use this skinny:**
1. Start with the 2.0 vocabulary and processes.
2. Read the 3.0 example carefully. That's the target.
3. Choose your demonstration mode and begin gathering evidence.
4. Pull additional skinnies if you hit a gap.
5. Check your scale tasks as you complete them.

---

*Skinny v1.0 — SDA Commons Wiki · June 2026*
*For the full anatomy of a skinny, see [[AGENTS.md#skinny-anatomy]]*

IMPORTANT: Fill in ALL bracketed sections with real, specific, student-readable content. No placeholders. Use concrete examples from Hammurabi's Code, Egyptian religious texts, early Hinduism/Buddhism. Every section must be complete and meaty — aim for 350-500 lines total."""
    },
    {
        "id": 2,
        "path": "/home/thinkstation/sda-wiki/skinnies/world-history/era-1/wh-6-12-3-political-systems-era1-skinny.md",
        "prompt": """Write a complete SDA skinny mini-lesson in clean markdown. Follow this exact structure and fill every bracketed section with real, specific, concrete content:

# How Political Systems in Ancient Greece and Rome Still Shape Us — Skinny

**Standard:** WH.6_12.3 — Analyze the effects of different political systems on people
**Era/Unit (if SS):** Era 1 — Emergence of Civilizations and Religions Around the Globe
**ELA Crosswalk:** 9-10.W.4 — Write to persuade; argument writing with evidence and counterclaims
**NDSBL Target:** 3.0 score
**Estimated Time:** 60–90 minutes
**Subject:** World History + ELA crosswalk

---

## What You Need to Know (Score 2.0)

Define these terms in plain student-readable language:
- Democracy (Athenian direct democracy vs. modern representative democracy)
- Republic (Roman Republic — what it means)
- Senate (Roman)
- Assembly (Athenian Ekklesia)
- Citizenship (who had it in Athens vs. Rome vs. now)
- Oligarchy
- Tyranny
- Veto (where this word comes from)
- Checks and balances
- Primary source (Pericles' Funeral Oration, Twelve Tables of Rome)

List 5 basic processes students should be able to do (checkboxes).
End with a specific 2.0 example: "A student who can..." — about identifying features of Athenian democracy from Pericles' Funeral Oration.

---

## The Standard (Score 3.0)

Write the full 3.0 section:
- Plain language explanation of what meeting WH.6_12.3 means
- A concrete 3.0 example: analyzing how Athenian democracy and/or the Roman Republic affected specific groups of people differently (citizens vs. non-citizens, men vs. women, enslaved people) using evidence from primary sources
- One clear sentence distinguishing 3.0 from 2.0

---

## Going Further (Score 4.0)

Write 3 specific transfer tasks connecting ancient political systems to modern democracy. Include one concrete 4.0 example that synthesizes across eras.

---

## CrashCourse Connection

**Video:** Ancient Greece — https://www.youtube.com/watch?v=OP4SL0hkRBE
**Also:** Roman Republic — https://www.youtube.com/watch?v=ePSME3kJBGQ

Write 3 specific realistic timestamps for these episodes with what happens and why it matters for WH.6_12.3.

**Watch Prompt:** As you watch, track: [specific annotation task about political systems and who they helped/hurt]

---

## Reading Library Connection

- [[reading-library/social-studies/pericles-funeral-oration]] — one sentence on connection
- [[reading-library/social-studies/twelve-tables-rome]] — one sentence on connection
- [[reading-library/social-studies/roman-republic-polybius]] — one sentence

---

## Demonstration of Learning — Choose One

| # | Mode | What You Do for This Specific Standard |
|---|------|----------------------------------------|
| 1 | **Written Assessment** | [Specific prompt: analyze how Athenian democracy or the Roman Republic affected a specific group — citizens, women, enslaved people, non-citizens — using evidence from at least one primary source] |
| 2 | **Extended Writing** | [Specific argument essay: 400-600 words arguing whether Athens or Rome created a more fair political system, using evidence from primary sources and acknowledging a counterclaim] |
| 3 | **Verbal Conversation** | [3 specific things to explain verbally about how Greek/Roman political systems worked and who they excluded] |
| 4 | **Visual/Creative** | [Specific visual task — annotated comparison chart or diagram of Athenian vs. Roman political structures with analysis of who held power] |
| 5 | **Multimedia/Performance** | [Specific podcast/video task — debate or documentary-style piece comparing the two systems] |
| 6 | **Portfolio Annotation** | [Specific portfolio annotation task using 2.0/3.0/4.0 language] |

---

## Deliverable Ideas (Your Studio Product)

1. **[Title]** — [Specific deliverable with format and real audience]
2. **[Title]** — [Second deliverable idea]
3. **[Title]** — [Third deliverable idea]

---

## Scale Tasks

- [ ] **2.0 task:** [Identify specific features of Athenian or Roman political system from a primary source]
- [ ] **3.0 task:** [Analyze how a specific political system affected different groups of people — with evidence]
- [ ] **4.0 task:** [Connect ancient political system to a modern democracy or argue about legacy]

---

## See Also

- [[standards/social-studies/world-history/era-1-civilizations]]
- [[standards/social-studies/world-history/standards-overview#WH.6_12.3]]
- [[standards/ela/writing-standards#9-10.W.4]] — W.4 argument writing crosswalk
- [[skinnies/ela9/w4-argument-writing-skinny]] — W.4 skinny
- [[skinnies/templates/research-skinny]]

---

**How to use this skinny:**
1. Start with the 2.0 vocabulary.
2. Read the 3.0 example. That's the target.
3. Choose your demonstration mode.
4. Pull additional skinnies if you hit a gap.
5. Check scale tasks as you go.

---

*Skinny v1.0 — SDA Commons Wiki · June 2026*

Fill ALL bracketed sections with specific, concrete, student-readable content. No placeholders. Aim for 350-500 lines."""
    },
    {
        "id": 3,
        "path": "/home/thinkstation/sda-wiki/skinnies/world-history/era-2/wh-6-12-3-medieval-political-skinny.md",
        "prompt": """Write a complete SDA skinny mini-lesson in clean markdown. Fill every section with real, specific, student-readable content. No placeholders.

# How Medieval Political Systems Controlled People — Skinny

**Standard:** WH.6_12.3 — Analyze the effects of different political systems on people
**Era/Unit (if SS):** Era 2 — Middle Ages and the Renaissance (~500–1600 CE)
**ELA Crosswalk:** 9-10.W.4 — Write to persuade; argument writing with evidence and counterclaims
**NDSBL Target:** 3.0 score
**Estimated Time:** 60–90 minutes
**Subject:** World History + ELA crosswalk

---

## What You Need to Know (Score 2.0)

Define these terms clearly in plain student language:
- Feudalism (the system, the hierarchy — king → lord → knight → serf)
- Vassal
- Fief
- Serf vs. peasant (what's the difference)
- Manorial system
- Pope / Papacy
- Excommunication (what it meant politically)
- Investiture Controversy (give a one-sentence plain explanation)
- Magna Carta (1215 — what it was and why it mattered)
- Common law
- Divine right of kings

List 5 basic processes students should be able to do (checkboxes).
End with a concrete 2.0 example: a student who can identify the roles in the feudal pyramid from a visual or primary source.

---

## The Standard (Score 3.0)

Write the full 3.0 section about WH.6_12.3 + Era 2:
- Plain language explanation
- Concrete 3.0 example: analyzing how feudalism AND Church authority together affected specific people (serfs, women, merchants, Jews, peasants) — using evidence from the Magna Carta or other primary sources
- Clear distinction between 3.0 and 2.0

---

## Going Further (Score 4.0)

Write 3 transfer tasks connecting medieval political systems to modern political structures or comparing to another era. Concrete 4.0 example.

---

## CrashCourse Connection

**Video:** The Dark Ages...How Dark Were They, Really? — https://www.youtube.com/watch?v=NX7monqP_-A
**Also:** Islam, the Quran, and the Five Pillars — https://www.youtube.com/watch?v=PnQLpGqQDTU (for Church/state comparison)

Write 3 realistic specific timestamps with content notes for the medieval/feudalism CrashCourse episode.

**Watch Prompt:** As you watch, track: [specific annotation task about who had power and who didn't in medieval society]

---

## Reading Library Connection

- [[reading-library/social-studies/magna-carta-1215]] — one sentence
- [[reading-library/social-studies/feudal-obligations-primary-source]] — one sentence
- [[reading-library/social-studies/pope-gregory-emperor-henry-correspondence]] — one sentence on investiture controversy

---

## Demonstration of Learning — Choose One

| # | Mode | What You Do for This Specific Standard |
|---|------|----------------------------------------|
| 1 | **Written Assessment** | [Specific prompt about feudalism, Church power, or Magna Carta — how did this political system help or harm a specific group of people? Use evidence.] |
| 2 | **Extended Writing** | [400-600 word argument essay: Was feudalism a fair political system? Take a position, use evidence, address a counterclaim.] |
| 3 | **Verbal Conversation** | [3 things to explain verbally about how medieval political systems worked and who they helped/hurt] |
| 4 | **Visual/Creative** | [Specific visual task — annotated feudal pyramid or Magna Carta analysis diagram] |
| 5 | **Multimedia/Performance** | [Specific podcast/debate task — argue whether the Magna Carta was a genuine step toward democracy or a self-serving document for nobles] |
| 6 | **Portfolio Annotation** | [Specific portfolio annotation task using 2.0/3.0/4.0 language connecting to WH.6_12.3 + Era 2] |

---

## Deliverable Ideas (Your Studio Product)

1. **[Title]** — [Specific deliverable with format and real audience — something a medieval historian or community member could engage with]
2. **[Title]** — [Second deliverable idea]
3. **[Title]** — [Third deliverable idea]

---

## Scale Tasks

- [ ] **2.0 task:** [Identify roles and obligations in the feudal system from a primary source or diagram]
- [ ] **3.0 task:** [Analyze how feudalism and/or Church authority affected a specific group — with specific evidence]
- [ ] **4.0 task:** [Evaluate: does the Magna Carta represent a genuine shift in political power, or just a limit on royal overreach? Connect to modern constitutional law.]

---

## See Also

- [[standards/social-studies/world-history/era-2-middle-ages]]
- [[standards/social-studies/world-history/standards-overview#WH.6_12.3]]
- [[standards/ela/writing-standards#9-10.W.4]]
- [[skinnies/ela9/w4-argument-writing-skinny]]
- [[skinnies/templates/research-skinny]]

---

*Skinny v1.0 — SDA Commons Wiki · June 2026*

Aim for 350-500 lines. All content specific and student-readable."""
    },
    {
        "id": 4,
        "path": "/home/thinkstation/sda-wiki/skinnies/world-history/era-3/wh-6-12-4-revolution-social-economic-skinny.md",
        "prompt": """Write a complete SDA skinny mini-lesson in clean markdown. All bracketed sections must be filled with specific, student-readable content.

# How the Age of Revolution Changed Social and Economic Life — Skinny

**Standard:** WH.6_12.4 — Analyze the influence of social, cultural, and economic development on individuals
**Era/Unit (if SS):** Era 3 — Age of Revolutions (~1400–1900)
**ELA Crosswalk:** 9-10.R.9 — Analyze informational/argumentative elements, author POV, bias, rhetorical techniques
**NDSBL Target:** 3.0 score
**Estimated Time:** 60–90 minutes
**Subject:** World History + ELA crosswalk

---

## What You Need to Know (Score 2.0)

Define these terms in plain student language:
- Revolution (political vs. social vs. economic)
- The Estates System (First, Second, Third Estate in France — who was in each)
- Bourgeoisie (middle class in the French Revolution context)
- Sans-culottes (who they were, what they wanted)
- Haitian Revolution (why it's unique — first successful slave revolt that created a nation)
- Toussaint Louverture (who he was)
- Mercantilism (how it created economic grievances)
- Social mobility (what it means, why it matters for revolution)
- Primary source bias (author's position shapes what they write — the R.9 connection)
- Propaganda

List 5 basic processes (checkboxes).
End with a concrete 2.0 example: a student who can identify the social class grievances in a primary source from the French Revolution.

---

## The Standard (Score 3.0)

Write the full 3.0 section:
- Plain language for WH.6_12.4 + Era 3
- Concrete 3.0 example: analyzing how the economic causes of the French Revolution and the social causes of the Haitian Revolution differently affected individuals — using primary source evidence and considering author POV/bias (R.9 crosswalk)
- Clear distinction between 3.0 and 2.0

---

## Going Further (Score 4.0)

Write 3 transfer tasks. Include one that compares the French and Haitian Revolutions in terms of who actually benefited socially and economically. Concrete 4.0 example.

---

## CrashCourse Connection

**Video:** The French Revolution — https://www.youtube.com/watch?v=lTTvKwCylFY
**Also:** The Haitian Revolution — https://www.youtube.com/watch?v=7KVT2oBFRpE

Write 3 specific timestamps for these episodes with what happens and why it matters for WH.6_12.4.

**Watch Prompt:** As you watch, track: [specific annotation task about social/economic causes and who was affected]

---

## Reading Library Connection

- [[reading-library/social-studies/declaration-rights-man-1789]] — one sentence on how this reveals bourgeois values and social aspirations
- [[reading-library/social-studies/haitian-declaration-independence-1804]] — one sentence on unique social/economic context
- [[reading-library/social-studies/olympe-de-gouges-declaration-woman]] — one sentence on bias and whose revolution it actually was

---

## Demonstration of Learning — Choose One

| # | Mode | What You Do for This Specific Standard |
|---|------|----------------------------------------|
| 1 | **Written Assessment** | [Specific prompt: How did the economic conditions of 18th-century France contribute to the outbreak of revolution? Use at least two specific pieces of evidence. Consider how the author's social class shapes what they emphasize in your sources.] |
| 2 | **Extended Writing** | [400-600 word analytical essay: Compare how the French Revolution and the Haitian Revolution affected individuals differently based on their social and economic position. Use primary source evidence and address author POV/bias (R.9 crosswalk).] |
| 3 | **Verbal Conversation** | [3 specific things to explain verbally: the economic causes of the French Revolution, why the Haitian Revolution was unique, and how to identify bias in a primary source from this era] |
| 4 | **Visual/Creative** | [Specific visual task — annotated diagram showing the social and economic conditions before and after one revolution, with analysis of who gained and who lost] |
| 5 | **Multimedia/Performance** | [Specific podcast task — interview format: voice two perspectives from different social classes on whether the French Revolution improved their lives] |
| 6 | **Portfolio Annotation** | [Specific portfolio annotation task with 2.0/3.0/4.0 language connecting to WH.6_12.4 + Era 3] |

---

## Deliverable Ideas (Your Studio Product)

1. **[Title]** — [Specific deliverable about revolutionary-era social/economic change — format and real audience]
2. **[Title]** — [Second deliverable idea — different format]
3. **[Title]** — [Third deliverable idea connecting to present-day economic inequality or social movements]

---

## Scale Tasks

- [ ] **2.0 task:** [Identify three social or economic causes of the French Revolution from a primary source. Write one sentence for each.]
- [ ] **3.0 task:** [Analyze how the social and economic conditions of 18th-century France and/or Haiti shaped the revolution — with specific evidence and attention to author POV/bias]
- [ ] **4.0 task:** [Compare how the French and Haitian Revolutions affected specific groups differently. Evaluate which revolution produced more genuine social change for ordinary people — and defend that argument with evidence.]

---

## See Also

- [[standards/social-studies/world-history/era-3-revolutions]]
- [[standards/social-studies/world-history/standards-overview#WH.6_12.4]]
- [[standards/ela/gr9-10-scales#9-10.R.9]]
- [[skinnies/ela9/r9-informational-argumentative-skinny]]
- [[skinnies/templates/research-skinny]]

---

*Skinny v1.0 — SDA Commons Wiki · June 2026*

Aim for 350-500 lines. All content specific, concrete, and student-readable."""
    },
    {
        "id": 5,
        "path": "/home/thinkstation/sda-wiki/skinnies/ela9/w4-argument-writing-skinny.md",
        "prompt": """Write a complete SDA skinny mini-lesson in clean markdown. This is the MOST IMPORTANT writing standard — used every other studio. Make it rich, practical, and example-driven.

# Writing to Persuade — Argument Writing Skinny

**Standard:** 9-10.W.4 — Write to persuade an audience by establishing relevant context, stating a clear position/thesis, incorporating valid and reliable evidence from a variety of sources to support specific claims and to refute counterclaims, and using logical reasoning to avoid fallacies.
**Era/Unit (if SS):** Active across all studios (W.4 is the argument writing standard — used in alternating studios)
**NDSBL Target:** 3.0 score
**Estimated Time:** 60–90 minutes
**Subject:** ELA

---

## What You Need to Know (Score 2.0)

Define ALL of these terms clearly in plain student language:
- Argument (in academic writing — not a fight)
- Thesis / Position statement (what it is and what makes one strong vs. weak)
- Context (why the reader needs background before the thesis)
- Claim (a statement that needs evidence to support it)
- Evidence (what counts: statistics, primary sources, expert quotes, historical examples)
- Counterclaim (the other side's best argument)
- Rebuttal (how you respond to the counterclaim)
- Logical fallacy — with 5 specific examples:
  * Ad hominem (attacking the person, not the argument)
  * Straw man (misrepresenting the other side)
  * Slippery slope (assuming extreme consequences)
  * Bandwagon (everyone else does it)
  * False dilemma (either/or when there are more options)
- Reliable source vs. unreliable source (for W.4 purposes)
- Warrant (the logical bridge between evidence and claim)

List 5 basic processes students should be able to do (checkboxes — concrete, completable).
End with a concrete 2.0 example: "A student who can write a thesis statement and identify two supporting pieces of evidence — but struggles to address the counterclaim effectively — is at 2.0."

---

## The Standard (Score 3.0)

**9-10.W.4 — Write to persuade an audience by establishing relevant context, stating a clear position/thesis, incorporating valid and reliable evidence from a variety of sources to support specific claims and to refute counterclaims, and using logical reasoning to avoid fallacies.**

Write the full 3.0 section:
- Clear explanation of what meeting W.4 means for a 9th grader
- A CONCRETE 3.0 example: show an actual example thesis + 2 evidence sentences + 1 counterclaim sentence + 1 rebuttal — taken from a realistic SDA studio context (e.g., "Was feudalism a fair political system?" or "Was the French Revolution successful?")
- One sentence distinguishing 3.0 from 2.0

---

## Going Further (Score 4.0)

Write 3 transfer tasks for W.4 that go beyond the standard — synthesis across studios, audience analysis, or meta-evaluation of argument structure. Concrete 4.0 example.

---

## CrashCourse Connection

**Video:** Crash Course English: The Persuasive Essay — https://www.youtube.com/watch?v=mMsKSPiMfCY
**Also:** Crash Course Philosophy: Fallacies — https://www.youtube.com/watch?v=IquO_TcMZIQ

Write 3 realistic specific timestamps for the persuasive essay or fallacies episodes.

**Watch Prompt:** As you watch, track: [specific annotation task about argument structure]

---

## Reading Library Connection

- [[reading-library/ela/declaration-of-independence-argumentative]] — one sentence on how the Declaration models W.4 argument structure
- [[reading-library/ela/mlk-letter-birmingham-jail]] — one sentence on counterclaim and rebuttal mastery

---

## The Anatomy of a W.4 Argument (Expanded Section)

[Write a detailed breakdown of the 5-part argument structure that W.4 requires. Use a table or structured format:

1. CONTEXT — What goes here? Why? Example from a real studio.
2. THESIS/POSITION — What makes it strong? Weak thesis vs. strong thesis example.
3. BODY CLAIMS + EVIDENCE — How many? What counts as evidence? Example with warrant.
4. COUNTERCLAIM — Why include it? How to introduce it fairly. Example sentence.
5. REBUTTAL — How to rebut without dismissing. Example sentence.

Include a WEAK example vs. STRONG example for the thesis.]

---

## Common Mistakes at Each Score Level

[Write a table or list of the most common W.4 mistakes at 2.0 and what moves them to 3.0:]
- Missing context
- Thesis that's a fact, not an argument
- Evidence without a warrant (just dropping a quote)
- No counterclaim
- Logical fallacy instead of reasoning

---

## Demonstration of Learning — Choose One

| # | Mode | What You Do for This Specific Standard |
|---|------|----------------------------------------|
| 1 | **Written Assessment** | [Specific argument prompt — student writes a short argument (300-400 words) responding to a debatable historical question, demonstrating all W.4 components] |
| 2 | **Extended Writing** | [500-700 word full argument essay on a debatable topic from the current studio — must include all W.4 components explicitly] |
| 3 | **Verbal Conversation** | [3 specific things to explain verbally: how the argument is structured, what evidence supports each claim, and how the counterclaim is addressed] |
| 4 | **Visual/Creative** | [Argument map / sketchnote showing the full W.4 structure for a specific argument — all components labeled and connected] |
| 5 | **Multimedia/Performance** | [Recorded debate or persuasive speech demonstrating W.4 — what it must include to count as evidence for this standard] |
| 6 | **Portfolio Annotation** | [Select an existing piece of argument writing from this or a previous studio. Annotate each section using W.4 language: "This is my context because... This is my thesis... This is my counterclaim + rebuttal..."] |

---

## Deliverable Ideas (Your Studio Product)

1. **[Title]** — [Specific deliverable using argument writing — op-ed, position paper, debate brief, persuasive letter to a real audience]
2. **[Title]** — [Different format and audience]
3. **[Title]** — [Third option connecting to real-world issues]

---

## Scale Tasks

- [ ] **2.0 task:** [Write a thesis statement AND identify a counterclaim for the same debatable question. Check: is your thesis an argument (not a fact)? Does your counterclaim represent the other side fairly?]
- [ ] **3.0 task:** [Write a complete W.4 argument (500+ words) with context, thesis, at least 2 claims with evidence and warrants, a counterclaim, and a rebuttal. Identify any logical fallacies you might be tempted to use — and avoid them.]
- [ ] **4.0 task:** [Revise your argument for a DIFFERENT audience (e.g., your argument was written for peers — now rewrite the context and evidence choices for a skeptical adult audience). Annotate what you changed and why.]

---

## See Also

- [[standards/ela/writing-standards#9-10.W.4]] — full standard with scale descriptors
- [[standards/ela/gr9-10-priority]] — priority standards overview
- [[standards/ela/crosswalk-ela-ss]] — W.4 crosswalk with WH/USH standards
- [[skinnies/ela9/w3-informational-writing-skinny]] — W.3 (informational writing — alternate studio)
- [[skinnies/templates/research-skinny]] — IR.1–IR.5 (finding sources for your argument)

---

*Skinny v1.0 — SDA Commons Wiki · June 2026*

Make this the richest and most complete skinny of all 8. Aim for 450-600 lines. Every section must be fully written with specific examples."""
    },
    {
        "id": 6,
        "path": "/home/thinkstation/sda-wiki/skinnies/ela9/w3-informational-writing-skinny.md",
        "prompt": """Write a complete SDA skinny mini-lesson in clean markdown. All content must be specific and student-readable.

# Writing to Inform and Explain — Skinny

**Standard:** 9-10.W.3 — Write to inform an audience and to explain complex information by creating a clear thesis and providing supporting claims, details, and evidence from a variety of relevant and reliable sources.
**Era/Unit (if SS):** Active in alternating studios (W.3 alternates with W.4 each studio)
**NDSBL Target:** 3.0 score
**Estimated Time:** 60–90 minutes
**Subject:** ELA

---

## What You Need to Know (Score 2.0)

Define these terms in plain student language:
- Informational writing (explain vs. persuade — what's the difference)
- Thesis (for informational writing — different from argument thesis)
- Supporting claim (what it is in explanatory writing)
- Evidence (what counts: statistics, expert quotes, primary sources, examples)
- Relevant source vs. irrelevant source
- Reliable source vs. unreliable source
- Paraphrase vs. direct quote (when to use each)
- Integration (weaving evidence into your writing, not just dropping it in)
- Synthesis (combining information from multiple sources into a coherent explanation)
- Complexity (what makes information "complex" in the W.3 sense)

List 5 basic processes students should be able to do (checkboxes).
End with a concrete 2.0 example: "A student who can write a clear thesis and list supporting evidence — but struggles to explain how the evidence supports the thesis — is at 2.0."

---

## The Standard (Score 3.0)

Write the full 3.0 section:
- Clear explanation of what meeting W.3 means
- Concrete 3.0 example: show a thesis + 2 body claim sentences + evidence integration from a realistic SDA studio context (e.g., explaining how the printing press changed information access in the Renaissance, or how the Industrial Revolution changed family life)
- Clear distinction between 3.0 and 2.0 (usually: 2.0 lists information; 3.0 explains the "how" and "why")

---

## Going Further (Score 4.0)

Write 3 transfer tasks for W.3. Include one that involves explaining a complex historical phenomenon to a non-expert audience. Concrete 4.0 example.

---

## CrashCourse Connection

**Video:** Crash Course English: The Informational Essay — find a relevant video
**Also:** Any CrashCourse history episode — use as a model of how experts explain complex history clearly

Write 3 realistic timestamps focused on how the narrator explains complex information accessibly.

**Watch Prompt:** As you watch, track: [specific annotation task about how complexity is explained]

---

## Reading Library Connection

- [[reading-library/ela/how-to-read-a-primary-source]] — one sentence
- [[reading-library/ela/evidence-integration-guide]] — one sentence

---

## W.3 vs. W.4: The Key Difference

[Write a clear, concrete comparison table or paragraph explaining:
- W.3 explains and informs — no thesis arguing a debatable position
- W.4 persuades — thesis is a debatable claim with counterclaims
- When you use each in SDA studios
- Example: "The printing press spread ideas faster" is a W.3 explanatory thesis. "The printing press was the most important cause of the Reformation" is a W.4 argument thesis.]

---

## Demonstration of Learning — Choose One

| # | Mode | What You Do for This Specific Standard |
|---|------|----------------------------------------|
| 1 | **Written Assessment** | [Specific informational prompt — explain a historical phenomenon using evidence from at least two sources] |
| 2 | **Extended Writing** | [400-600 word explanatory essay on a topic from the current studio — clear thesis, supporting claims, integrated evidence from multiple reliable sources] |
| 3 | **Verbal Conversation** | [3 specific things to explain verbally about informational writing structure and source integration] |
| 4 | **Visual/Creative** | [Specific visual task — concept map or annotated outline showing how the thesis, claims, and evidence connect] |
| 5 | **Multimedia/Performance** | [Specific podcast or explainer video task — explain a complex historical topic to a specific non-expert audience] |
| 6 | **Portfolio Annotation** | [Select an existing informational piece. Annotate using W.3 language: thesis, claims, evidence sources, integration quality] |

---

## Deliverable Ideas (Your Studio Product)

1. **[Title]** — [Informational deliverable idea — explainer essay, research report, Wikipedia-style entry for the SDA wiki]
2. **[Title]** — [Second deliverable idea — different format/audience]
3. **[Title]** — [Third deliverable idea]

---

## Scale Tasks

- [ ] **2.0 task:** [Write a clear informational thesis and identify three supporting claims. Label each claim and name the source of evidence you will use for it.]
- [ ] **3.0 task:** [Write a complete W.3 informational essay (400+ words) with a clear thesis, at least 2 claims with integrated evidence from 2+ reliable sources, and explanations connecting each piece of evidence to your thesis.]
- [ ] **4.0 task:** [Revise your informational piece for a specific non-expert audience (elementary students, local newspaper readers, museum visitors). Annotate what you changed to make complex information accessible — and why those changes work.]

---

## See Also

- [[standards/ela/writing-standards#9-10.W.3]]
- [[standards/ela/crosswalk-ela-ss]]
- [[skinnies/ela9/w4-argument-writing-skinny]] — argument writing (W.4)
- [[skinnies/templates/research-skinny]] — IR.1–IR.5 research skills

---

*Skinny v1.0 — SDA Commons Wiki · June 2026*

Aim for 350-450 lines. All content specific, concrete, student-readable."""
    },
    {
        "id": 7,
        "path": "/home/thinkstation/sda-wiki/skinnies/ela9/r9-informational-argumentative-skinny.md",
        "prompt": """Write a complete SDA skinny mini-lesson in clean markdown. All content must be specific and student-readable. No placeholders.

# Analyzing Informational and Argumentative Texts — Skinny

**Standard:** 9-10.R.9 — Analyze the development and interaction of informational and argumentative elements over the course of a nonfiction text and how they impact purpose using textual evidence to support the analysis. (Includes: author's POV and bias; multiple accounts in different media; argumentative reasoning and rhetorical techniques.)
**Era/Unit (if SS):** Active across all studios when reading primary sources or nonfiction
**NDSBL Target:** 3.0 score
**Estimated Time:** 60–90 minutes
**Subject:** ELA

---

## What You Need to Know (Score 2.0)

Define these terms clearly in plain student language:
- Informational text (what counts)
- Argumentative text (what makes it an argument vs. just information)
- Author's purpose (inform / persuade / entertain — and how to identify it)
- Point of view (POV) — the author's position or perspective
- Bias — definition, and how to distinguish it from mere opinion
- Rhetorical techniques — define 4 specifically:
  * Ethos (credibility/authority appeals)
  * Pathos (emotional appeals)
  * Logos (logical/evidence appeals)
  * Repetition / parallel structure (how repetition works in political speeches)
- Textual evidence (what it is, why it's required for analysis — not just summary)
- Primary source vs. secondary source (why the distinction matters for bias)
- Multiple accounts (same event, different sources — why they differ)

List 5 basic processes (checkboxes).
End with a concrete 2.0 example: "A student who can identify the author's main claim and note one piece of evidence — but can't explain HOW the evidence supports the author's purpose — is at 2.0."

---

## The Standard (Score 3.0)

**9-10.R.9 — Analyze the development and interaction of informational and argumentative elements over the course of a nonfiction text and how they impact purpose using textual evidence to support the analysis.**

Write the full 3.0 section:
- Clear explanation of what meeting R.9 means in practice
- Concrete 3.0 example: analyzing a specific primary source — for instance, Pericles' Funeral Oration OR the Declaration of the Rights of Man (1789) OR MLK's "Letter from Birmingham Jail." Show what a 3.0 analysis looks like: identify author POV, note 2 specific rhetorical techniques with textual evidence, explain how those choices serve the author's purpose.
- One sentence distinguishing 3.0 from 2.0

---

## Going Further (Score 4.0)

Write 3 transfer tasks for R.9. Include one comparing two primary sources from different time periods addressing the same topic. Concrete 4.0 example.

---

## CrashCourse Connection

**Video:** Crash Course English: Reading Nonfiction — relevant episode
**Also:** Crash Course Rhetoric — relevant episode on rhetorical techniques

Write 3 realistic timestamps focused on how to identify rhetorical techniques and author POV.

**Watch Prompt:** As you watch, track: [specific annotation task — every time you hear an appeal to ethos, pathos, or logos, note the timestamp and quote]

---

## Reading Library Connection

- [[reading-library/ela/pericles-funeral-oration]] — one sentence on R.9 application
- [[reading-library/ela/mlk-letter-birmingham-jail]] — one sentence on how it models argument analysis for R.9
- [[reading-library/social-studies/declaration-rights-man-1789]] — one sentence on bias and POV analysis

---

## How to Annotate for R.9 (Practical Guide)

[Write a practical annotation guide — what to mark when reading a nonfiction/argumentative text for R.9:
1. Mark the author's main claim (underline)
2. Identify rhetorical techniques (label in margin: E/P/L for ethos/pathos/logos)
3. Note bias indicators — word choice, what's left out, who the author is
4. Track how the argument develops — does early evidence build to a conclusion?
5. For multiple accounts: use two different colors for two sources]

---

## Demonstration of Learning — Choose One

| # | Mode | What You Do for This Specific Standard |
|---|------|----------------------------------------|
| 1 | **Written Assessment** | [Specific analytical prompt: Choose one primary source from the current studio. Analyze the author's point of view, identify two rhetorical techniques with textual evidence, and explain how these choices serve the author's purpose.] |
| 2 | **Extended Writing** | [400-600 word analytical essay comparing TWO primary sources on the same topic — analyzing how different authors' POV and rhetorical choices lead to different accounts of the same event] |
| 3 | **Verbal Conversation** | [3 things to explain verbally: the author's purpose and POV, two specific rhetorical techniques from the text, and how bias shapes what's included or excluded] |
| 4 | **Visual/Creative** | [Annotated primary source analysis — mark up a primary source with color-coded annotations showing POV, rhetorical techniques, bias indicators, and evidence for purpose] |
| 5 | **Multimedia/Performance** | [Podcast episode: read and analyze a primary source aloud, explaining the rhetorical techniques and author bias as you go — teach-back format] |
| 6 | **Portfolio Annotation** | [Select an existing analytical piece. Annotate where you identified author POV, rhetorical techniques, and bias — using R.9 language explicitly at 2.0/3.0/4.0 level] |

---

## Deliverable Ideas (Your Studio Product)

1. **[Title]** — [Primary source analysis deliverable — annotated document, analytical essay, or visual essay comparing two historical accounts]
2. **[Title]** — [Second deliverable idea — different format]
3. **[Title]** — [Third deliverable idea — media literacy angle: analyze a modern news article or political speech using the same R.9 tools]

---

## Scale Tasks

- [ ] **2.0 task:** [Read a primary source. Identify the author's main claim. Find two pieces of evidence. Write one sentence for each explaining what the evidence says (not yet how it serves the purpose).]
- [ ] **3.0 task:** [Analyze a primary source using R.9: identify the author's POV and bias, label two rhetorical techniques with textual evidence, and explain in 2-3 sentences how these choices serve the author's purpose.]
- [ ] **4.0 task:** [Compare two primary sources on the same historical topic. Analyze how different author POV, bias, and rhetorical choices produce different accounts. Evaluate which account is more effective for a specific audience — and defend that evaluation.]

---

## See Also

- [[standards/ela/gr9-10-scales#9-10.R.9]]
- [[standards/ela/crosswalk-ela-ss]] — R.9 crosswalk with WH primary source analysis
- [[skinnies/world-history/era-1/wh-6-12-2-belief-systems-skinny]] — R.9 applied to ancient religious texts
- [[skinnies/world-history/era-3/wh-6-12-4-revolution-social-economic-skinny]] — R.9 applied to revolutionary era sources
- [[skinnies/templates/research-skinny]]

---

*Skinny v1.0 — SDA Commons Wiki · June 2026*

Aim for 400-500 lines. All content specific, concrete, student-readable. Include a practical annotation guide section."""
    },
    {
        "id": 8,
        "path": "/home/thinkstation/sda-wiki/skinnies/ela9/ir-research-bundle-skinny.md",
        "prompt": """Write a complete SDA skinny mini-lesson in clean markdown. This is the Research Toolbox — active EVERY studio. Make it comprehensive and practical.

# The Research Toolbox — IR.1–IR.5 Bundle Skinny

**Standards:** 9-10.IR.1 through 9-10.IR.5 (bundled — all five active every studio)
- **IR.1** — Develop pertinent research questions and narrow or broaden the inquiry.
- **IR.2** — Gather and interpret relevant information from primary and secondary sources for a variety of purposes.
- **IR.3** — Organize relevant information from a variety of sources.
- **IR.4** — Evaluate the credibility of a source based on bias, perspective, and purpose.
- **IR.5** — Integrate information from sources using a standardized format.
**Era/Unit (if SS):** Active every studio — the backbone of all research in SDA
**NDSBL Target:** 3.0 score
**Estimated Time:** 90–120 minutes (full research process)
**Subject:** ELA (Inquiry and Research)

---

## What You Need to Know (Score 2.0)

Define all of these terms in plain student language:

**IR.1 — Research Questions:**
- Research question (what makes one good vs. bad)
- Too broad vs. too narrow (with examples)
- Essential question vs. research question (what's the difference in SDA)
- Narrowing an inquiry

**IR.2 — Gathering Information:**
- Primary source (original document, artifact, eyewitness account)
- Secondary source (analysis, textbook, documentary about events)
- Database vs. search engine (why it matters)
- Keyword search strategy
- Boolean operators (AND, OR, NOT — basic)

**IR.3 — Organizing Information:**
- Note-taking (what to capture, what to leave out)
- Source log (why you keep one)
- Annotation (what to write in the margins)
- Outline vs. concept map

**IR.4 — Evaluating Credibility:**
- SIFT method (Stop, Investigate the source, Find better coverage, Trace claims)
- Bias vs. perspective (distinction)
- Purpose of a source (who made it, why, for whom)
- Lateral reading (checking a source by looking at what others say about it)

**IR.5 — Citations:**
- MLA format basics (author, title, publication, date, URL)
- In-text citation (author page) vs. Works Cited
- Plagiarism vs. paraphrase vs. direct quote
- Why citation matters (it's not just a rule — it's intellectual honesty)

List 5 basic processes (checkboxes) — one for each IR standard.
End with a concrete 2.0 example: "A student who can find sources and list them — but can't evaluate whether the sources are credible or explain how the evidence connects to their inquiry question — is at 2.0."

---

## The Standards (Score 3.0)

Write the full 3.0 section for all 5 IR standards together:
- Explain what meeting the full IR.1–IR.5 bundle means in an SDA studio context
- Concrete 3.0 example: show what a complete research process looks like for a specific studio (e.g., Studio 1 "Power & Belief" — a student develops a focused research question about how early religions justified political authority, finds 3 credible sources (primary + secondary), organizes notes with annotations, evaluates each source for bias, and cites all sources in MLA format)
- Clear distinction between 3.0 and 2.0

---

## Going Further (Score 4.0)

Write 3 transfer tasks for the IR bundle. Include one that involves evaluating conflicting sources and synthesizing a coherent argument from them. Concrete 4.0 example.

---

## CrashCourse Connection

**Video:** Crash Course Navigating Digital Information — https://www.youtube.com/watch?v=pLlv2o6UfTU
**Also:** Crash Course Study Hall: Research Papers — relevant episode

Write 3 realistic timestamps focused on source credibility, SIFT, or research organization.

**Watch Prompt:** As you watch, track: [specific annotation task about evaluating sources]

---

## Reading Library Connection

- [[reading-library/ela/how-to-read-a-primary-source]] — one sentence
- [[reading-library/ela/lateral-reading-guide]] — one sentence
- [[reading-library/ela/mla-citation-quick-reference]] — one sentence

---

## The Research Process in SDA — Week by Week

[Write a table or structured guide showing when each IR standard is most active in the studio lifecycle:

| Studio Week | Phase | IR Standards Active | What You're Doing |
|------------|-------|--------------------|--------------------|
| Week 1 | Launch | IR.1 | Developing your research question |
| Week 2 | Dig | IR.2, IR.4 | Finding and evaluating sources |
| Week 2-3 | Dig/Build | IR.3 | Organizing your notes and source log |
| Week 3-4 | Build/Shape | IR.2, IR.3 | Deepening research and refining |
| Week 5 | Finish | IR.5 | Final citations, Works Cited |]

---

## Source Log Template

[Write a practical source log template students can copy into their notebook or Google Doc:

**Source Entry:**
- Full citation (MLA):
- Type (primary / secondary):
- Main claim or finding:
- Key quote (with page/paragraph number):
- Credibility evaluation: Who made it? Why? For whom? Bias?
- How does this connect to my research question?]

---

## The SIFT Method in Practice

[Write a concrete walkthrough of SIFT applied to a specific source — e.g., a Wikipedia article about the French Revolution, a .com website about medieval feudalism. Show what each step produces.]

---

## Demonstration of Learning — Choose One

| # | Mode | What You Do for This Specific Standard |
|---|------|----------------------------------------|
| 1 | **Written Assessment** | [Specific prompt: Describe your complete research process for this studio — your research question (IR.1), 3 sources with credibility evaluations (IR.2 + IR.4), your organization system (IR.3), and your citations (IR.5). Explain decisions at each step.] |
| 2 | **Extended Writing** | [Annotated bibliography — for each of 4 sources, write a paragraph explaining what it contains, why it's credible, how it connects to your research question, and its full MLA citation — demonstrating IR.1-IR.5 together] |
| 3 | **Verbal Conversation** | [Walk your advisor through your research process: your research question and how you narrowed it, how you found and evaluated 3 sources, how you organized your notes, and your citation format] |
| 4 | **Visual/Creative** | [Research map — visual showing your research question at center, sources branching out with credibility notes, connections to your inquiry angle, and how you organized information across sources] |
| 5 | **Multimedia/Performance** | [Teach-back video or podcast: explain to a younger student how to evaluate whether a source is credible — demonstrate SIFT using a real source] |
| 6 | **Portfolio Annotation** | [Annotate your source log and notes using IR.1-IR.5 language: "I narrowed my question when... (IR.1). I chose this source because... (IR.2, IR.4). I organized by... (IR.3). My citation format is... (IR.5)"] |

---

## Deliverable Ideas (Your Studio Product)

1. **Annotated Bibliography** — A formal document listing 5+ sources with credibility analysis and connection to inquiry question. Audience: your advisor and future SDA students who study this topic.
2. **Research Portfolio** — A curated set of your source log, annotated notes, and a reflection on how your research question evolved — with a final Works Cited page. Audience: portfolio defense at exhibition.
3. **Source Credibility Workshop** — Create a mini-lesson teaching other students how to evaluate sources using SIFT. Include 3 example sources with your credibility analysis. Audience: your SDA cohort.

---

## Scale Tasks

- [ ] **2.0 task:** [Write a research question for your studio inquiry. Test it: is it too broad? Too narrow? Find two sources. List them in MLA format.]
- [ ] **3.0 task:** [Complete your source log for 4 sources (at least 1 primary). For each: MLA citation, credibility evaluation using SIFT, key quote, and connection to your research question. Organize your notes using a system you can explain.]
- [ ] **4.0 task:** [Identify two sources on the same topic that contradict each other. Evaluate which is more credible and why — using SIFT and lateral reading. Write a paragraph synthesizing what you can conclude from both, acknowledging the contradiction.]

---

## See Also

- [[standards/ela/gr9-10-scales#9-10.IR.1]]
- [[standards/ela/gr9-10-scales#9-10.IR.2]]
- [[standards/ela/gr9-10-scales#9-10.IR.3]]
- [[standards/ela/gr9-10-scales#9-10.IR.4]]
- [[standards/ela/gr9-10-scales#9-10.IR.5]]
- [[standards/ela/crosswalk-ela-ss]] — how IR bundle connects to WH/USH research tasks
- [[skinnies/ela9/w4-argument-writing-skinny]] — using research sources in argument writing
- [[skinnies/ela9/r9-informational-argumentative-skinny]] — evaluating sources for R.9 analysis

---

*Skinny v1.0 — SDA Commons Wiki · June 2026*

Make this the most comprehensive research guide in the wiki. Aim for 450-600 lines. All content specific and student-readable. Include the week-by-week table, source log template, and SIFT walkthrough."""
    },
]

def main():
    results = []
    for skinny in SKINNIES:
        sid = skinny["id"]
        path = skinny["path"]
        filename = os.path.basename(path)
        print(f"\n[{sid}/8] Generating: {filename}")
        print(f"  Model: gemma4:12b | Path: {path}")

        start = time.time()
        content = generate(skinny["prompt"])
        elapsed = time.time() - start

        # Write file
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(content)

        line_count = content.count("\n") + 1
        print(f"  ✓ Generated: {filename} ({line_count} lines, {elapsed:.0f}s)")
        results.append((filename, line_count, elapsed))

    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"{'File':<55} {'Lines':>6} {'Time':>6}")
    print("-"*60)
    for fname, lines, t in results:
        print(f"{fname:<55} {lines:>6} {t:>5.0f}s")
    print(f"\nTotal: {len(results)} skinnies generated")

if __name__ == "__main__":
    main()
