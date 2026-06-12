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

## Pose Quality Gate

Before a skeleton image enters a report, check it as a user-facing coaching artifact:

- the skeleton belongs to the trainee, not a coach, spotter, mirror reflection, or bystander
- the movement's main chain is usable, such as hip-knee-ankle for lower-body work or shoulder-elbow-wrist for upper-body work
- the selected frames show distinct movement stages rather than four nearly identical moments
- the key position is visible, especially bottom depth, peak contraction, lockout, or controlled return

If the fast full-video pass produces a bad skeleton, do not use it in the final report. Try a higher-quality keyframe pass, crop/mask bystanders if practical, or reselect clearer frames. Use unannotated or manually marked frames only after the higher-quality keyframe pass is also unsuitable. The final report should still avoid naming internal engines or explaining tracking failures.

## Bystanders And Spotters

When a spotter or coach is close to the lifter:

1. Prefer a cleaner set of the same movement if available.
2. Try a higher-quality keyframe pose review before giving up on skeleton evidence.
3. Try cropping or masking the bystander when practical.
4. If body points remain unreliable, use implement trajectory and visual review.
5. In the user-facing report, do not write technical failure details. Say only what can be judged from the visible movement.

## Keyframe Display

- Use 4 stages per important movement.
- Use 2 columns for portrait-friendly 4-stage grids unless a different layout is clearly better.
- Keep the image and movement commentary in the same report card.
- If all frames look the same, reselect frames.
- Preserve the source orientation: portrait videos should remain portrait, and landscape videos should remain landscape. Do not squeeze portrait footage into a wide strip.

## Subtask Delegation

For long training days, split review work:

- one reviewer for sample selection
- one reviewer for high-risk compound lifts
- one reviewer for machine/isolation lifts
- one reviewer for report quality and terminology

The final author must still audit all conclusions before delivery.
