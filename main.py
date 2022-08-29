import argparse
from animation import AnimatedScatter
from driver import parameters_for_simulation

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     conflict_handler='resolve')
    parser.add_argument('--num_bodies', type=int, required = True)
    args = parser.parse_args()
    bodies, axis_range, timescale = parameters_for_simulation(args.num_bodies)
    a = AnimatedScatter(bodies, args.num_bodies, axis_range, timescale)
    a.show()

