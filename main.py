from collections import namedtuple
import statistics as stat
from math import pi

import lcg
from histogram import draw_histogram

LcgParameters = namedtuple('LcgParameters', ['initial', 'multiplyer', 'base'])

def main():
    base = int(input("m: "))
    initial = int(input("R0: "))
    multiplyer = int(input("a: "))
    params = LcgParameters(multiplyer=multiplyer, initial=initial, base=base)
    result = list(lcg.random_vector(100000, params))
    mean = stat.mean(result)
    print('mean (reference value = 1/2 = {}): {}; delta: {} '.format(0.5, mean, abs(mean - 0.5)))
    variance = stat.variance(result)
    print('variance (reference value = 1/12 = {}): {}; delta: {}'.format(1/12, variance, abs(1/12 - variance)))
    ratio = lcg.uniform_ratio(result)
    print('uniform ration (reference value = pi/4 = {}): {}; delta: {}'.format(pi/4, ratio, abs(pi/4 - ratio)))
    period = lcg.period(lambda length: lcg.random_vector(length, params))
    if not period:
        print('Can not find period')
    else:
        print('period:', period)
    aperiodic_interval = lcg.aperiodic_interval(lambda length: lcg.random_vector(length, params), period)
    if not aperiodic_interval:
        print('Can not find aperiodic interval')
    else:
        print('aperiodic interval:', aperiodic_interval)
    draw_histogram(result)


if __name__ == '__main__':
    main()
