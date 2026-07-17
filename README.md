# Reachy Mini Scripts

Personal collection of Python scripts for [Reachy Mini](https://github.com/pollen-robotics/reachy_mini) (Lite, USB-connected).

## Setup

```bash
python3 -m venv reachy_mini_env
source reachy_mini_env/bin/activate
pip install -r requirements.txt
```

The Reachy Mini daemon must be running and the robot connected before running any script.

## Scripts

| Script | Description |
|---|---|
| `scripts/hello.py` | Minimal connection check — wiggles the antennas. |
| `scripts/head_tracking.py` | Detects the largest face in the robot's camera feed (OpenCV Haar cascade) and points the head at it via `look_at_image`. |

Run with:

```bash
python scripts/hello.py
python scripts/head_tracking.py
```

## Notes

- `opencv-python` is pinned to `<5` — 5.x removed `cv2.CascadeClassifier` from the
  Python bindings this project depends on for face detection.
- See `AGENTS.md` for conventions used by AI coding agents in this repo.
