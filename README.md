# Three-joint arm kinematics

This program calculates the position of a robot arm's tip from its three joint angles. This is called forward kinematics. It is useful when you know how far the joints have turned and want to know where the arm will reach.

## The arm model

The first joint turns the arm around its base. This motion is called yaw. The second and third joints raise or lower the two moving links. This motion is called pitch.

The three lengths have different roles.

- L1 is the height of the base. Its default length is 10.
- L2 is the first moving link. Its default length is 15.
- L3 is the second moving link. Its default length is 10.

All three lengths must use the same unit. If you enter centimeters, the final position is also in centimeters.

## How the calculation works

The program converts the angles from degrees to radians. It then builds a 4 by 4 transformation matrix for each joint. Each matrix describes a rotation and a movement in space. Multiplying the matrices gives the final position and direction of the arm's tip.

When all angles are zero, the moving links point along the positive X axis at the base height. Positive yaw turns toward positive Y. Positive pitch lifts the links toward positive Z. The zero-angle position with the default lengths is X = 25, Y = 0, and Z = 10.

This program calculates the arm's geometry. It does not move servos or check the physical limits of the joints.

## Try it

Use Python 3.11 or newer. Open a terminal in this project's folder and create a virtual environment. This keeps its packages separate from your other Python projects.

```sh
python -m venv .venv
```

On Windows, activate it with this command.

```sh
.venv\Scripts\activate
```

On macOS or Linux, use this command instead.

```sh
source .venv/bin/activate
```

Then install the packages the project needs.

```sh
python -m pip install -r requirements.txt
```

```sh
python kinematics.py 45 30 90
python kinematics.py 0 0 0 --lengths 10 15 10
```

The three angle inputs are base yaw, shoulder pitch, and elbow pitch, in that order. The output contains X, Y, and Z coordinates along with the full transformation matrix.

## Tests

```sh
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

The tests check several known arm positions, invalid lengths, and whether the rotation matrices stay mathematically valid.
