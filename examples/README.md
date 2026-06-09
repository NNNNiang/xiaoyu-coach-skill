# Examples

This folder contains small public samples for quickly testing Xiaoyu Coach.

The examples are intentionally short, compressed, muted, and stripped of phone metadata. Do not add private training videos here unless the person in the video has explicitly approved public release.

## Available Samples

| Folder | Exercise | Video | Duration | Filming angle | Purpose |
| --- | --- | --- | ---: | --- | --- |
| `barbell-squat-50kg-side-rear/` | Barbell squat | `barbell_squat_50kg_side_rear_25s.mp4` | 25.07 s | Vertical phone video from a side-rear 30-45 degree angle | Free-weight stability, squat depth, bar path, and safety-priority review |
| `bench-press-front-oblique/` | Barbell bench press | `bench_press_front_oblique_15s.mp4` | 15.77 s | Vertical phone video from a front-oblique / foot-end diagonal angle | Quick single-exercise report test and filming-angle demonstration |
| `dumbbell-rdl-side/` | Dumbbell Romanian deadlift / soft-knee straight-leg deadlift | `dumbbell_rdl_side_18s.mp4` | 17.47 s | Vertical phone video from a side angle | Hip hinge, back-position review, bottom-range safety, and filming-angle demonstration |
| `open-elbow-row-front-oblique/` | Open-elbow row | `open_elbow_row_front_oblique_24s.mp4` | 23.97 s | Vertical phone video from a front-oblique angle | Row path, elbow height, trunk stability, and camera-angle demonstration |

## Quick Test Prompt

After installing the skill, ask Codex:

```text
Use $xiaoyu-coach to analyze examples/bench-press-front-oblique as a single-exercise assessment. Generate an HTML movement assessment and include filming-angle feedback.
```

Other useful prompts:

```text
Use $xiaoyu-coach to analyze examples/barbell-squat-50kg-side-rear as a single-exercise assessment. Focus on squat depth, trunk stability, bar path, and safety priority.
```

```text
Use $xiaoyu-coach to analyze examples/dumbbell-rdl-side as a single-exercise assessment. Focus on hip hinge, back position, bottom range, and filming-angle feedback.
```

```text
Use $xiaoyu-coach to analyze examples/open-elbow-row-front-oblique as a single-exercise assessment. Focus on elbow path, shoulder position, trunk stability, and filming-angle feedback.
```

Expected output:

- a concise HTML action assessment
- comments on movement setup, path, control, and safety
- filming-angle feedback explaining what the current angle shows well and what a better angle would reveal
