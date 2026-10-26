import argparse
import json
import math
import numpy as np

def forward(angles, lengths=(10.0, 15.0, 10.0)):
    if len(angles) != 3 or len(lengths) != 3:
        raise ValueError('Supply three angles and three lengths')
    if not all(math.isfinite(v) for v in (*angles, *lengths)) or min(lengths) <= 0:
        raise ValueError('Angles must be finite and lengths positive')
    yaw, shoulder, elbow = map(math.radians, angles)
    height, upper, forearm = lengths
    c, s = math.cos(yaw), math.sin(yaw)
    t1 = np.array([[c, -s, 0, 0], [s, c, 0, 0], [0, 0, 1, height], [0, 0, 0, 1]])
    def pitch_link(angle, length):
        c, s = math.cos(angle), math.sin(angle)
        return np.array([[c, 0, -s, length*c], [0, 1, 0, 0],
                         [s, 0, c, length*s], [0, 0, 0, 1]])
    t2 = pitch_link(shoulder, upper)
    t3 = pitch_link(elbow, forearm)
    return t1 @ t2 @ t3

def main():
    parser = argparse.ArgumentParser(description='Forward kinematics for a yaw-pitch-pitch arm')
    parser.add_argument('angles', type=float, nargs=3, metavar='ANGLE')
    parser.add_argument('--lengths', type=float, nargs=3, default=(10, 15, 10))
    args = parser.parse_args()
    try:
        transform = forward(args.angles, args.lengths)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps({'position': dict(zip(('x', 'y', 'z'), transform[:3, 3].tolist())),
                      'transform': transform.tolist()}, indent=2))

if __name__ == '__main__':
    main()
