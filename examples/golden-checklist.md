# Golden Example Checklist

These examples are the public regression set for Xiaoyu Coach. They are not just demo videos; they define the minimum output quality expected from the skill.

## How To Use

1. Pick one example folder.
2. Read that folder's `README.md`, `expected_findings.md`, and `expected_report.html`.
3. Generate a single-exercise assessment with `$xiaoyu-coach`.
4. Validate the report with `xiaoyu-coach/scripts/validate_report.py`.
5. Compare the report against the expected findings and baseline report.

## What A Passing Report Must Do

- Include a safety-priority section.
- Pair movement evidence with coach-style commentary.
- Give specific next-session corrections.
- Include filming-angle feedback.
- Avoid internal tool names and frame-selection language.
- Avoid copying issues from other examples or users.
- Avoid generic exercise encyclopedia text that is not tied to the current video.
- Preserve the expected report's structure unless the skill's report standard has intentionally changed.

## Current Golden Examples

| Folder | Primary capability tested |
| --- | --- |
| `bench-press-front-oblique/` | Bench press path, wrist/elbow setup, safety setup limits, front-oblique camera tradeoff |
| `barbell-squat-50kg-side-rear/` | Free-weight squat safety, depth, trunk stability, bar path, side-rear camera tradeoff |
| `dumbbell-rdl-side/` | Hip hinge, back position, bottom-range safety, side camera tradeoff |
| `open-elbow-row-front-oblique/` | Open-elbow row path, shoulder position, trunk stability, front-oblique camera tradeoff |

## Suggested Regression Prompt

```text
Use $xiaoyu-coach to analyze examples/<folder> as a single-exercise assessment. Generate an HTML movement assessment. Use the sample README and expected_findings.md as the test target, but do not copy their wording directly into the report.
```

## When Updating The Skill

Run the golden examples after changes to:

- `SKILL.md`
- `references/report-standards.md`
- `references/safety-and-coaching.md`
- `references/video-analysis-workflow.md`
- `assets/html_report_template.html`
- report generation prompts or scripts

If a generated report violates an expected finding, update the skill or workflow. Update `expected_findings.md` or `expected_report.html` only when the intended coaching standard has genuinely changed.
