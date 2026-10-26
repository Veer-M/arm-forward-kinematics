# Three-joint arm kinematics

A small forward kinematics calculator for a base-yaw, shoulder-pitch, elbow-pitch arm. Give it three angles and it returns the tool position and the full transform matrix.

## Run it

Use Python 3.11 or newer. Run these commands from this repository's folder.

```sh
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
# source .venv/bin/activate
python -m pip install -r requirements.txt
```

```sh
python kinematics.py 45 30 90
python kinematics.py 0 0 0 --lengths 10 15 10
```

## How it works and current limits

L1 is the vertical base height. L2 and L3 are the two moving links. Zero angles point along +X at height L1. Positive yaw turns toward +Y; positive pitch lifts toward +Z. All lengths use the same unit. This computes geometry only and does not drive servos or enforce joint limits.

## Tests

```sh
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

Tests check known arm positions, rotation-matrix orthogonality, and invalid lengths.
