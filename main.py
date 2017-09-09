from collections import namedtuple
import statistics as stat
from math import pi

import lcg
from histogram import draw_histogram

LcgParameters = namedtuple('LcgParameters', ['initial', 'multiplyer', 'base'])


def print_result(name, actual_result, reference_value_representation='', reference_value=None):
    if actual_result is not None:
        result = '{}: {}'.format(name, actual_result)
        if reference_value:
            result += ' (reference value = {}; delta: {})'.format(reference_value_representation + ' = ' + str(reference_value) 
                if reference_value_representation
                else
                    reference_value
                , abs(reference_value - actual_result)
            )
    else:
        result = 'Can not find {}'.format(name)
    print(result)


def read_lcg_parameters():
    return LcgParameters(
        base=int(input("m: ")),
        initial=int(input("R0: ")),
        multiplyer=int(input("a: "))
    )


def main():
    params = read_lcg_parameters()
    result = list(lcg.random_vector(100000, params))
    print_result('mean', stat.mean(result), reference_value=1/2, reference_value_representation='1/2')
    print_result('variance', stat.variance(result), reference_value=1/12, reference_value_representation='1/12')
    print_result('2K/N', lcg.uniform_ratio(result), reference_value=pi/4, reference_value_representation='pi/4')
    period = lcg.period(lambda length: lcg.random_vector(length, params))
    print_result('period', period)
    if period:
        print_result('aperiodic interval', lcg.aperiodic_interval(lambda length: lcg.random_vector(length, params), period))
    draw_histogram(result)


if __name__ == '__main__':
    main()
