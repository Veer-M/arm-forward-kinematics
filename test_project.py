import numpy as np
import pytest
from kinematics import forward

@pytest.mark.parametrize('angles,position', [((0,0,0),(25,0,10)), ((90,0,0),(0,25,10)), ((0,90,0),(0,0,35)), ((0,0,180),(5,0,10))])
def test_known_positions(angles, position):
    t = forward(angles)
    np.testing.assert_allclose(t[:3,3], position, atol=1e-10)
    np.testing.assert_allclose(t[:3,:3].T @ t[:3,:3], np.eye(3), atol=1e-10)

def test_invalid_length():
    with pytest.raises(ValueError):
        forward((0,0,0), (10,0,10))
