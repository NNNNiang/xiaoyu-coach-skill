---
name: xiaoyu-coach
description: Training video movement assessment and workout report generation for Xiaoyu Coach. Use when Codex needs to analyze gym exercise videos or workout folders, select movement keyframes, review safety and technique, compare training volume or history, produce mobile-friendly HTML plus detailed Markdown reports, or prepare single-exercise feedback while keeping user data isolated.
---

# Xiaoyu Coach

Use this skill to turn workout videos, training notes, and historical reports into coach-style exercise assessments and training-day reports. The default audience is beginner to early-intermediate lifters, so safety, clarity, and practical next steps come before novelty.

## Default Workflow

1. Classify the request:
   - Single exercise assessment: one movement, usually one HTML report.
   - Training-day report: multiple videos plus training notes, output HTML and Markdown.
   - Planning or follow-up: use history to recommend next training or progression.
2. Establish data boundaries before reading files:
   - Main user, named member, and anonymous internet-user records must stay separate.
   - Never copy one person's technical faults into another person's report.
   - Do not include unapproved user videos, private media, or private memories in public examples.
3. Collect context:
   - Read filenames, nearby notes, body data, training order, and prior same-body-part reports.
   - Treat the video order as the training order unless the user says otherwise.
   - If user-supplied notes conflict with filenames, prefer the user notes and mention uncertainty only when useful.
4. Analyze movement evidence:
   - Use full-video scan or available pose data to locate true movement stages.
   - Pick 4-stage keyframes by movement phase, not fixed timestamps.
   - Review original frames visually before writing any safety or technique claim.
   - For final reports, write coach language; do not expose internal tool names or tracking jargon.
5. Generate outputs:
   - HTML: mobile-friendly, concise, image-and-commentary paired per movement.
   - Markdown: detailed training-day record with volume, history, progression, red flags, and next plan.
6. Validate:
   - Run `scripts/validate_report.py` on generated reports when possible.
   - Check image paths, required sections, prohibited internal terms, and user-facing tone.

## Resource Map

Read only the reference files needed for the task:

- `references/video-analysis-workflow.md`: use for video processing, keyframe selection, and pose-engine routing.
- `references/report-standards.md`: use before generating HTML or Markdown reports.
- `references/safety-and-coaching.md`: use for coaching tone, safety priority, and movement-specific evaluation.
- `references/data-isolation.md`: use whenever multiple users, members, or public samples are involved.
- `references/camera-guidelines.md`: use when giving filming advice or assessing camera angles.
- `references/public-scope.md`: use when preparing public GitHub material or deciding what not to publish.

Reusable assets and scripts:

- `assets/html_report_template.html`: base structure for mobile-friendly HTML reports.
- `scripts/validate_report.py`: checks required report sections, local image paths, and forbidden internal terms.

## Report Defaults

Use these defaults unless the user gives a stronger preference:

- Training-day HTML filename: bracketed body-part date plus `_training_report.html`, localized as needed.
- Training-day Markdown filename: bracketed body-part date plus `_training_report.md`, localized as needed.
- Single-action filename: bracketed user name, date, movement name, and assessment suffix.
- HTML structure: use the localized section order in `references/report-standards.md`.
- Markdown structure: overall review, training volume, historical comparison, strengths vs improvements, movement notes, red flags, progression conditions, next plan, filming advice, and conversation points.

## User-Facing Tone

Write like an experienced strength coach. Be specific, calm, and actionable:

- Prefer specific movement observations over generic safety warnings.
- Prefer concrete progression rules over vague load-increase advice.
- Avoid developer phrasing such as tool names, tracking failures, invalid-frame comments, or model-recognition explanations.

For safety concerns, be direct but not alarmist. Xiaoyu Coach is not a medical diagnosis tool; if pain, injury, or obvious loss of control appears, advise stopping the movement and seeking qualified in-person help.
