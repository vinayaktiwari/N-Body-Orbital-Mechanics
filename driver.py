from body import Body, SUN_MASS, AU, ONE_DAY
import numpy as np
from animation import AnimatedScatter


def parameters_for_simulation(num_bodies):
    sun = Body('sun', mass=SUN_MASS, p=np.array([0.0, 0.0, 0.0]))
    earth = Body('earth', mass=5.9742 * 10 ** 24, p=np.array([-1 * AU, 0.0, 0.0]),
                 v=np.array([0.0, 29.783 * 1000, 0.0]))
    venus = Body('venus', mass=4.8685 * 10 ** 24, p=np.array([0.723 * AU, 0.0, 0.0]),
                 v=np.array([0.0, -35.0 * 1000, 0.0]))

    asteroid = Body('asteroid', mass=4.8685 * 10, p=np.array([0.0, 0.0, 3 * AU]),
                    v=np.array([0.0, -35.0 * 100, 0.0]))

    black_hole1 = Body('black_hole', mass=5 * SUN_MASS, p=np.array([0.0, 3 * AU, 0.0]))

    black_hole2 = Body('black_hole', mass=5 * SUN_MASS, p=np.array([3 * AU, 0.0, 0.0]))

    black_hole3 = Body('black_hole', mass=5 * SUN_MASS, p=np.array([0.0, 0.0, 3 * AU]))

    axis_range = (-3 * AU, 3 * AU)
    timescale = ONE_DAY
    return [sun, earth, venus, asteroid, black_hole1, black_hole2, black_hole3][:num_bodies], axis_range, timescale
