# Agent Guide for This Repo

This is a personal collection of Reachy Mini scripts (Python, on-robot/laptop side),
not the SDK itself. For the full SDK agent guide, see
https://github.com/pollen-robotics/reachy_mini/blob/main/AGENTS.md.

## Session Start

Check `agents.local.md` (gitignored, not in this repo's history) for robot type,
environment setup status, and notes from previous sessions. If it doesn't exist,
this is a fresh machine — recreate the venv per README.md.

## Conventions

- Scripts live in `scripts/`, run against the SDK in `reachy_mini_env/` (local venv,
  gitignored, install with `pip install -r requirements.txt`).
- Before adding a new non-trivial script or feature, write a short `plan.md`
  (gitignored scratch file) describing the approach, and confirm with the user
  before implementing.
- Verify SDK methods actually exist (`python -c "from reachy_mini import ReachyMini; print(dir(ReachyMini))"`)
  before relying on them — don't assume a method exists because it "sounds right."
