# Third-Party Notices

This file separates the current public Skill repository from the broader
local or future production analysis stack.

## Current Public Repository

At the time of this notice, the public `xiaoyu-coach-skill` repository has
no third-party runtime dependency manifest. Its validation scripts use only
the Python standard library:

- `argparse`
- `re`
- `sys`
- `pathlib`

The public Skill instructions may describe video-analysis workflows, but
this repository does not bundle MediaPipe, OpenCV, MMPose, OpenPose,
FFmpeg, model weights, or private production services.

## Planned or Local Analysis Stack

If future releases add executable analysis tooling, review and preserve
the licenses for every direct and transitive dependency. The following
tools have been considered or used in local experiments:

| Tool | Typical license | Production note |
| --- | --- | --- |
| MediaPipe | Apache-2.0 | Suitable as a default commercial-friendly pose-analysis route, subject to model and package notices. |
| OpenCV | Apache-2.0 for modern OpenCV 4.x | Suitable for frame extraction, image processing, annotation, and reporting utilities. |
| MMPose / OpenMMLab tooling | Apache-2.0 | Check each model config, checkpoint, and dataset term before commercial use. |
| NumPy | BSD-style permissive license | Suitable for numeric analysis. |
| Pillow | MIT-CMU / permissive PIL-style license | Suitable for image generation and composition. |
| PyTorch | BSD-style license | Code is generally permissive; model weights and datasets may have separate terms. |
| FFmpeg | LGPL/GPL depending on build options | Audit the exact binary and codecs before bundling or distributing. |
| OpenPose | Non-commercial research license | Do not use in paid products or commercial services without explicit commercial authorization. |

## Production Policy

- Do not add OpenPose to the default paid product pipeline unless a
  commercial license has been obtained and documented.
- Prefer commercial-friendly dependencies for the default route.
- Treat model weights, datasets, and generated sample media as separately
  licensed assets, even when the surrounding code is permissively licensed.
- Keep third-party notices in sync whenever dependencies are added.
