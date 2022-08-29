import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from body import points_for_bodies, norm_forces_for_bodies, move


class AnimatedScatter:

    def __init__(self, bodies, num_planets, axis_range, timescale):
        self.bodies = bodies
        self.num_planets = num_planets
        self.axis_range = axis_range
        self.timescale = timescale
        self.stream = self.data_stream()
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        self.fig = fig
        self.ax = ax
        self.force_norm_factor = None
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=10,
                                           init_func=self.setup_plot, blit=False)

    def setup_plot(self):
        colors = ['red', 'orange', 'blue', 'brown', 'black', 'black', 'black']

        xi, yi, zi, ui, vi, wi = next(self.stream)

        self.scatter = self.ax.scatter(xi, yi, zi, c=colors[: self.num_planets], s=200)

        self.quiver = self.ax.quiver(xi, yi, zi, ui, vi, wi, length=1)

        FLOOR = self.axis_range[0]
        CEILING = self.axis_range[1]
        self.ax.set_xlim3d(FLOOR, CEILING)
        self.ax.set_ylim3d(FLOOR, CEILING)
        self.ax.set_zlim3d(FLOOR, CEILING)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        return self.scatter, self.quiver

    def quiver_force_norm_factor(self):
        axis_length = np.abs(self.axis_range[1]) + np.abs(self.axis_range[0])
        return np.amax(np.array([b.f for b in self.bodies])) / (axis_length / 10)

    def data_stream(self):
        while True:
            move(self.bodies, self.timescale)
            if not self.force_norm_factor:
                self.force_norm_factor = self.quiver_force_norm_factor()
                print('factor ', self.force_norm_factor)
            x, y, z = points_for_bodies(self.bodies)
            u, v, w = norm_forces_for_bodies(self.bodies, self.force_norm_factor)
            yield x, y, z, u, v, w

    def update(self, i):
        x_i, y_i, z_i, u_i, v_i, w_i = next(self.stream)

        self.scatter._offsets3d = (x_i, y_i, z_i)

        segments = np.array([(b.p, b.p + b.f / self.force_norm_factor) for b in self.bodies])
        self.quiver.set_segments(segments)

        plt.draw()
        return self.scatter, self.quiver

    def show(self):
        plt.show()
