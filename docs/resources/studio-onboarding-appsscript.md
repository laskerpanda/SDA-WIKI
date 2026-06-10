# Studio Onboarding — Google Forms + Apps Script

**SDA Commons · South High School**

Every studio cycle begins with a student submitting a Google Form. The form triggers an Apps Script that generates a Studio Contract Google Doc and saves it to Drive.

---

## Step 1 — Create the Google Form

**Before adding any questions:** go to Form Settings → **Responses tab** → turn OFF "Collect email addresses." Google Forms enables this by default. If it's on, student Google account emails are logged — that's a FERPA problem. Turn it off first.

Also turn OFF "Limit to 1 response" — it requires sign-in and ties the response to a Google account.

Create a new Google Form with these exact fields (in order):

| Question | Type | Required |
|----------|------|----------|
| Student ID (your school ID number — no names) | Short answer | Yes |
| Select your inquiry angle | Multiple choice (options added per studio) | Yes |
| How will you demonstrate your learning? | Multiple choice (6 options below) | Yes |
| Describe your deliverable | Paragraph | Yes |
| What is your guiding research question? | Paragraph | Yes |
| Target proficiency score | Multiple choice: 2.0 / 3.0 / 4.0 | Yes |

**Demo mode options (copy these exactly):**
1. Written Assessment — focused written response to a prompt
2. Extended Writing — standalone essay or analytical piece
3. Verbal Conversation — talk through your understanding with your advisor
4. Visual/Creative — sketchnote, diagram, or infographic
5. Multimedia/Performance — podcast, video, or formal presentation
6. Portfolio Annotation — curate existing work with written reflection

---

## Step 2 — Set Up the Apps Script

In the Google Form: **⋮ menu → Script editor**

Paste this code, then fill in the constants at the top:

```javascript
// ============================================================
// SDA Studio Contract Generator
// Paste into Google Form Script Editor
// ============================================================

// FILL THESE IN before deploying:
const STUDIO_TITLE = "Power & Belief";           // current studio name
const ESSENTIAL_QUESTION = "How did early religions justify political authority?";
const WH_STANDARD = "WH.6_12.2";
const ERA_UNIT = "Era 1 — Emergence of Civilizations";
const ELA_STANDARD_1 = "9-10.R.9";
const ELA_STANDARD_2 = "9-10.W.3";
const WRITING_TYPE = "Explanatory (W.3)";
const DRIVE_FOLDER_ID = "YOUR_FOLDER_ID_HERE";  // ID from Drive folder URL
const NOTIFY_EMAIL = "YOUR_EMAIL_HERE";          // Reese's email for digest

// ============================================================

function onFormSubmit(e) {
  const responses = e.values;
  // e.values[0] = timestamp (no email column — email collection must be OFF)
  // If email collection is accidentally on, indices shift by 1 and email leaks into the doc.
  // Double-check Form Settings → Responses → Collect email addresses = OFF
  const timestamp   = responses[0];
  const studentId   = responses[1].trim().replace(/[^a-zA-Z0-9_-]/g, ''); // sanitize — IDs only
  const angle       = responses[2];
  const demoMode    = responses[3];
  const deliverable = responses[4];
  const researchQ   = responses[5];
  const targetScore = responses[6];

  // Hard stop: if studentId looks like an email address, something is misconfigured
  if (studentId.includes('@')) {
    MailApp.sendEmail(NOTIFY_EMAIL, '[SDA] FORM CONFIG ERROR',
      'A submission contained an email address in the Student ID field. Check that "Collect email addresses" is OFF in Form Settings.');
    return;
  }

  // Create the contract doc
  const doc = DocumentApp.create(`SDA Contract — ${studentId} — ${STUDIO_TITLE}`);
  const body = doc.getBody();

  body.appendParagraph("STUDIO CONTRACT")
    .setHeading(DocumentApp.ParagraphHeading.HEADING1);

  body.appendParagraph(`Student ID: ${studentId}`);
  body.appendParagraph(`Date: ${new Date(timestamp).toLocaleDateString()}`);
  body.appendParagraph(`Studio: ${STUDIO_TITLE}`);
  body.appendParagraph(`Essential Question: ${ESSENTIAL_QUESTION}`);

  body.appendParagraph("").appendHorizontalRule();

  body.appendParagraph("STANDARDS")
    .setHeading(DocumentApp.ParagraphHeading.HEADING2);
  body.appendParagraph(`Social Studies: ${WH_STANDARD} + ${ERA_UNIT}`);
  body.appendParagraph(`ELA Reading: ${ELA_STANDARD_1}`);
  body.appendParagraph(`ELA Writing: ${ELA_STANDARD_2} — ${WRITING_TYPE}`);
  body.appendParagraph(`Research: 9-10.IR.1–5 (active every studio)`);

  body.appendParagraph("").appendHorizontalRule();

  body.appendParagraph("MY STUDIO PLAN")
    .setHeading(DocumentApp.ParagraphHeading.HEADING2);
  body.appendParagraph(`Inquiry Angle: ${angle}`);
  body.appendParagraph(`Guiding Research Question: ${researchQ}`);
  body.appendParagraph(`Demonstration of Learning: ${demoMode}`);
  body.appendParagraph(`Deliverable: ${deliverable}`);
  body.appendParagraph(`Target Proficiency Score: ${targetScore}`);

  body.appendParagraph("").appendHorizontalRule();

  body.appendParagraph("PACE SHEET — 6 WEEKS")
    .setHeading(DocumentApp.ParagraphHeading.HEADING2);

  const paceData = [
    ["Week", "Phase", "My Goal This Week", "Done?"],
    ["1", "LAUNCH", "Submit this contract. Select sources. Write first draft of research question.", ""],
    ["2", "DIG",    "Annotate 3+ sources. Pull skinnies for gaps. Start evidence log.", ""],
    ["3", "BUILD",  "First draft of deliverable. Demonstration of learning work begins.", ""],
    ["4", "SHAPE",  "Peer feedback. Revision. Advisor check-in.", ""],
    ["5", "FINISH", "Complete demonstration of learning. Finalize deliverable.", ""],
    ["6", "PUBLISH","Exhibition. Reflection. Archive submission.", ""],
  ];

  const table = body.appendTable(paceData);
  table.getRow(0).editAsText().setBold(true);

  body.appendParagraph("").appendHorizontalRule();
  body.appendParagraph("Student signature (type your ID to confirm): _______________");
  body.appendParagraph("Advisor review: _______________");

  doc.saveAndClose();

  // Move to the designated Drive folder
  const file = DriveApp.getFileById(doc.getId());
  const folder = DriveApp.getFolderById(DRIVE_FOLDER_ID);
  folder.addFile(file);
  DriveApp.getRootFolder().removeFile(file);

  // Email digest to Reese
  MailApp.sendEmail({
    to: NOTIFY_EMAIL,
    subject: `[SDA] New contract: ${studentId} — ${STUDIO_TITLE}`,
    body: `Student ID: ${studentId}\nAngle: ${angle}\nDemo mode: ${demoMode}\nDeliverable: ${deliverable}\nResearch Q: ${researchQ}\nTarget: ${targetScore}\n\nContract saved to Drive.`
  });
}

// ============================================================
// HOW TO DEPLOY:
// 1. Fill in the constants at the top.
// 2. Click the clock icon (Triggers) → Add Trigger
//    Function: onFormSubmit
//    Event source: From form
//    Event type: On form submit
// 3. Authorize when prompted.
// ============================================================
```

---

## Step 3 — Get the Drive Folder ID

1. Open Google Drive → navigate to `The Commons/Studio Archive/2026-27/World History/`
2. The folder ID is the long string in the URL: `drive.google.com/drive/folders/`**`THIS_PART`**
3. Paste it into `DRIVE_FOLDER_ID` in the script

---

## Step 4 — Deploy

1. In Script Editor: **Clock icon (Triggers) → Add Trigger**
2. Function: `onFormSubmit`
3. Event source: From form
4. Event type: On form submit
5. Authorize when prompted (use your school Google account)

---

## Step 5 — Distribute the Form

- Get the form's shareable link → shorten via QR code (qr-code-generator.com or similar)
- Print QR code or display on classroom screen on Studio Launch day
- Post link in Headrush for the active studio

---

## Updating for Each New Studio

At the start of each cycle, open Script Editor and update the constants at the top:
- `STUDIO_TITLE`
- `ESSENTIAL_QUESTION`
- `WH_STANDARD` / `ERA_UNIT`
- `ELA_STANDARD_1` / `ELA_STANDARD_2`
- `WRITING_TYPE`
- `DRIVE_FOLDER_ID` (if saving to a new subfolder)

Also update the **inquiry angle options** in the form itself (the multiple choice question).

---

*Studio Onboarding · SDA Commons Wiki · South High School*
