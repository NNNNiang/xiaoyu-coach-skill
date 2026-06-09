# Xiaoyu Coach Skill

小鱼教练是一个面向普通训练者的训练视频动作评估与训练复盘 Codex Skill。它帮助使用者基于训练视频、训练记录和历史报告，生成安全优先、教练口吻、适合手机阅读的 HTML 报告，以及更详细的 Markdown 训练日报。

## Positioning

Xiaoyu Coach is not a replacement for a doctor, physical therapist, or in-person coach. It is a local-first workflow for reviewing gym training videos, especially for 0-3 year beginner and early-intermediate lifters.

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
├── README.md
├── .gitignore
└── xiaoyu-coach/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/html_report_template.html
    ├── references/
    │   ├── camera-guidelines.md
    │   ├── data-isolation.md
    │   ├── public-scope.md
    │   ├── report-standards.md
    │   ├── safety-and-coaching.md
    │   └── video-analysis-workflow.md
    └── scripts/validate_report.py
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

## Public Scope

This repository intentionally includes the reusable skeleton:

- report structure
- safety priority rules
- data isolation rules
- public workflow references
- generic HTML template
- report validation script

It intentionally excludes:

- real user videos
- private training memories
- private reports
- full commercial prompts
- payment or production service code
- API keys, local credentials, cookies, or tokens

## Report Validation

After generating a report, run:

```powershell
python .\xiaoyu-coach\scripts\validate_report.py path\to\report.html
python .\xiaoyu-coach\scripts\validate_report.py path\to\report.md
```

The validator checks required sections, local image paths, and internal terms that should not appear in final user-facing reports.

## Release Notes

This is an experimental public skill skeleton. Before publishing a public release, choose a license, audit examples for privacy, and make sure all sample data is synthetic or explicitly approved for release.
