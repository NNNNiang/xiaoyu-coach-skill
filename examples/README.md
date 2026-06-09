# Examples

This folder contains small public samples for quickly testing Xiaoyu Coach.

The examples are intentionally short, compressed, muted, and stripped of phone metadata. Do not add private training videos here unless the person in the video has explicitly approved public release.

## Available Samples

| Folder | Exercise | Video | Duration | Filming angle | Purpose |
| --- | --- | --- | ---: | --- | --- |
| `bench-press-front-oblique/` | Barbell bench press | `bench_press_front_oblique_15s.mp4` | 15.77 s | Vertical phone video from a front-oblique / foot-end diagonal angle | Quick single-exercise report test and filming-angle demonstration |

## Quick Test Prompt

After installing the skill, ask Codex:

```text
Use $xiaoyu-coach to analyze examples/bench-press-front-oblique as a single-exercise assessment. Generate an HTML movement assessment and include filming-angle feedback.
```

Expected output:

- a concise HTML action assessment
- comments on bench press setup, pressing path, control, and safety
- filming-angle feedback explaining what the current angle shows well and what a better angle would reveal
