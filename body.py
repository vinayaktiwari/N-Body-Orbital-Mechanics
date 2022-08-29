import itertools
import numpy as np


G = 6.67428e-11
AU = (149.6e6 * 1000)
SUN_MASS = 1.98892 * 10**30
ONE_DAY = 24*3600


class Body:

    def __init__(self, name, mass, p, v=(0.0, 0.0, 0.0)):
        self.name = name
        self.mass = mass
        self.p = p
        self.v = v
        self.f = np.array([0.0, 0.0, 0.0])

    def __str__(self):
        return 'Body {}'.format(self.name)

    def attraction(self, other):
        assert self is not other
        diff_vector = other.p - self.p
        distance = norm(diff_vector)
        print(distance)
        assert np.abs(distance) > 10**4, 'Bodies collided!'
        f_tot = G * self.mass * other.mass / (distance**2)
        f = f_tot * diff_vector / norm(diff_vector)
        return f


def norm(x):
    return np.sqrt(np.sum(x**2))


def move(bodies, timestep):
    pairs = itertools.combinations(bodies, 2)
    # Initialize force vectors
    for b in bodies:
        b.f = np.array([0.0, 0.0, 0.0])
    # Calculate force vectors
    for b1, b2 in pairs:
        f = b1.attraction(b2)
        b1.f += f
        b2.f -= f
    # Update velocities based on force, update positions based on velocity
    for body in bodies:
        body.v += body.f / body.mass * timestep
        body.p += body.v * timestep
        print(body.name, body.p, body.v, body.f)
    print('')


def points_for_bodies(bodies):
    x0 = np.array([body.p[0] for body in bodies])
    y0 = np.array([body.p[1] for body in bodies])
    z0 = np.array([body.p[2] for body in bodies])
    return x0, y0, z0


def norm_forces_for_bodies(bodies, norm_factor):
    u0 = np.array([body.f[0] for body in bodies])
    v0 = np.array([body.f[1] for body in bodies])
    w0 = np.array([body.f[2] for body in bodies])
    return u0/norm_factor, v0/norm_factor, w0/norm_factor



