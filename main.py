from collections import namedtuple
from statistics import mean, variance
from math import pi

from lcg import get_random_vector, get_uniform_ratio
from histogram import draw_histogram

LcgParameters = namedtuple('LcgParameters', ['initial', 'multiplyer', 'base'])

def main():
    base = int(input("m: "))
    initial = int(input("R0: "))
    multiplyer = int(input("a: "))
    params = LcgParameters(multiplyer=multiplyer, initial=initial, base=base)
    result = list(get_random_vector(100000, params))
    print('mean: ', mean(result))
    print('variance: ', variance(result))
    ratio = get_uniform_ratio(result)
    print('uniform ration (pi/4 = {}): {}; delta: {}'.format(pi/4, ratio, abs(pi/4 - ratio)))
    draw_histogram(result)
    

if __name__ == '__main__':
    main()
