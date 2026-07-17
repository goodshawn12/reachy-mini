# Reachy Mini Scripts

Personal collection of Python scripts for [Reachy Mini](https://github.com/pollen-robotics/reachy_mini) (Lite, USB-connected).

## Setup (macOS)

Follows the [official installation guide](https://huggingface.co/docs/reachy_mini/SDK/installation).

### 1. Prerequisites

- **Python 3.10–3.12** (this repo targets 3.12)
- **Homebrew**, **git**, **git-lfs**
- **[uv](https://docs.astral.sh/uv/)** — fast Python package/venv manager

```bash
# Homebrew (skip if already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# git + git-lfs
brew install git git-lfs
git lfs install

# uv
curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install 3.12 --default
```

### 2. Virtual environment + SDK

```bash
uv venv reachy_mini_env --python 3.12
source reachy_mini_env/bin/activate
uv pip install -r requirements.txt
```

> `requirements.txt` pins `reachy_mini` and `opencv-python<5` — see Notes below.

The Reachy Mini daemon must be running and the robot connected (USB, Lite) before running any script.

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
