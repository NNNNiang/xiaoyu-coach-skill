# Video Analysis Workflow

Use this file when the task includes exercise videos or keyframe selection.

## Pipeline

1. Inventory videos and training notes.
2. Preserve training order from upload order or filenames unless the user gives a correction.
3. Run the available full-video pose or computer-vision pass.
4. Use continuous signals to find candidate movement stages:
   - pressing: top, descent/bottom, press midpoint, lockout
   - rowing/pulldown: stretch, pull midpoint, contraction, return
   - squat/deadlift: top, descent/hinge, bottom, ascent/return
   - isolation: start, concentric midpoint, peak, eccentric return
5. Extract 4-stage keyframes. Do not rely on fixed timestamps.
6. Visually review large frames. Replace frames that are blurry, duplicate, occluded, or from the wrong person.
7. Use original video and keyframes together for final coaching judgment.

## Pose Engines

Use whatever engines are available in the environment. A useful division is:

- full-video fast scan for timing, trajectories, and candidate stages
- higher-quality keyframe pose review for a small set of selected frames
- image processing for cropping, marking, trajectory overlays, or excluding bystanders

If different engines disagree, prefer original-video visual review and clearly visible frames.

## Bystanders And Spotters

When a spotter or coach is close to the lifter:

1. Prefer a cleaner set of the same movement if available.
2. Try cropping or masking the bystander when practical.
3. If body points remain unreliable, use implement trajectory and visual review.
4. In the user-facing report, do not write technical failure details. Say only what can be judged from the visible movement.

## Keyframe Display

- Use 4 stages per important movement.
- Use 2 columns for portrait-friendly 4-stage grids unless a different layout is clearly better.
- Keep the image and movement commentary in the same report card.
- If all frames look the same, reselect frames.

## Subtask Delegation

For long training days, split review work:

- one reviewer for sample selection
- one reviewer for high-risk compound lifts
- one reviewer for machine/isolation lifts
- one reviewer for report quality and terminology

The final author must still audit all conclusions before delivery.
