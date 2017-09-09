from collections import namedtuple
from statistics import mean, variance
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
    print('mean: ', mean(result))
    print('variance: ', variance(result))
    ratio = lcg.uniform_ratio(result)
    print('uniform ration (pi/4 = {}): {}; delta: {}'.format(pi/4, ratio, abs(pi/4 - ratio)))
    period = lcg.period(lambda length, initial: lcg.random_vector(length, params._replace(initial=initial)))
    draw_histogram(result)
    if not period:
        print('Can not find period')
    else:
        print('period:', period)


if __name__ == '__main__':
    main()
