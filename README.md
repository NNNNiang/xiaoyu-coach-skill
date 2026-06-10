# Xiaoyu Coach Skill

Xiaoyu Coach is a Codex Skill for training-video movement assessment and
workout report generation. It helps turn workout videos, training notes,
and historical reports into safety-first, coach-style HTML and Markdown
reports.

The public repository is a reusable Skill skeleton. It is designed for
testing, contribution, and integration experiments without exposing private
training memories, private videos, or commercial service internals.

## Positioning

Xiaoyu Coach is not a replacement for a doctor, physical therapist, or
in-person coach. It is a local-first workflow for reviewing gym training
videos, especially for 0-3 year beginner and early-intermediate lifters.

Core outputs:

- single-exercise movement assessment
- full training-day HTML report
- detailed Markdown training report
- safety priority and red-flag review
- training volume and progression guidance
- filming-angle suggestions

## Repository Layout

```text
xiaoyu-coach-skill/
|- README.md
|- LICENSE
|- NOTICE
|- BRAND.md
|- THIRD_PARTY_NOTICES.md
|- examples/
|  |- LICENSE.md
|  |- README.md
|  |- golden-checklist.md
|  |- barbell-squat-50kg-side-rear/
|  |- bench-press-front-oblique/
|  |- dumbbell-rdl-side/
|  `- open-elbow-row-front-oblique/
`- xiaoyu-coach/
   |- SKILL.md
   |- agents/openai.yaml
   |- assets/html_report_template.html
   |- references/
   |  |- camera-guidelines.md
   |  |- data-isolation.md
   |  |- public-scope.md
   |  |- report-standards.md
   |  |- safety-and-coaching.md
   |  `- video-analysis-workflow.md
   `- scripts/
      |- validate_examples.py
      `- validate_report.py
```

## Install Locally

Copy the `xiaoyu-coach/` folder into your Codex skills directory, for example:

```powershell
Copy-Item -Recurse .\xiaoyu-coach "$env:USERPROFILE\.codex\skills\xiaoyu-coach"
```

Then ask Codex:

```text
Use $xiaoyu-coach to analyze this workout video folder and generate HTML plus Markdown reports.
```

## Quick Test Examples

This repo includes small public sample clips in `examples/`.

Current samples include:

- barbell bench press
- barbell squat
- dumbbell Romanian deadlift / soft-knee straight-leg deadlift
- open-elbow row

All sample clips are compressed vertical MP4 files, muted, and stripped of
phone/location metadata.

Each sample folder includes:

- `expected_findings.md`: bilingual Chinese/English expected observations
  and common misjudgments to avoid.
- `expected_report.html`: bilingual Chinese/English baseline report for
  quick visual and structural comparison.

Use these files as lightweight regression targets when changing the Skill.

After installing the Skill, try one sample:

```text
Use $xiaoyu-coach to analyze examples/bench-press-front-oblique as a single-exercise assessment. Generate an HTML movement assessment and include filming-angle feedback.
```

See `examples/README.md` for the full sample list and prompts.
See `examples/golden-checklist.md` for the regression checklist.

## Public Scope

This repository intentionally includes the reusable skeleton:

- report structure
- safety priority rules
- data isolation rules
- public workflow references
- generic HTML template
- report validation scripts
- explicitly approved, compressed, metadata-stripped public sample clips

It intentionally excludes:

- unapproved or private user videos
- private training memories
- private reports
- full commercial prompts
- payment or production service code
- API keys, local credentials, cookies, or tokens

## License, Brand, and Examples

Source code, scripts, templates, and general documentation are licensed
under the Apache License 2.0. See `LICENSE`.

Important boundaries:

- `NOTICE` explains attribution and scope.
- `BRAND.md` reserves the Xiaoyu Coach name, localized names, logos,
  avatars, mascot artwork, and confusingly similar product identity.
- `examples/LICENSE.md` applies extra restrictions to public example videos,
  preview images, expected findings, and expected reports.
- `THIRD_PARTY_NOTICES.md` records the current dependency status and the
  production policy for analysis engines such as MediaPipe, OpenCV, MMPose,
  FFmpeg, and OpenPose.

In short: the public Skill skeleton is open source; the Xiaoyu Coach brand,
private knowledge base, private user data, and commercial service internals
are not.

## Report Validation

After generating a report, run:

```powershell
python .\xiaoyu-coach\scripts\validate_report.py path\to\report.html
python .\xiaoyu-coach\scripts\validate_report.py path\to\report.md
```

The validator checks required sections, local image paths, and internal terms
that should not appear in final user-facing reports.

To validate the public example folder structure, run:

```powershell
python .\xiaoyu-coach\scripts\validate_examples.py .\examples
```

## Release Notes

This is an experimental public Skill skeleton. Before publishing a tagged
release, audit examples for privacy, validate all golden examples, and keep
dependency notices current.
