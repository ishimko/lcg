from collections import namedtuple
import statistics as stat
from math import pi
import sys

import lcg
from distributions import ExponentialDistribution, GammaDistribution, GaussianDistribution, UniformDistribution, TriangularDistribution, SimpsonDistribution
from histogram import draw_histogram
from reader import read_positive_int


LcgParameters = namedtuple('LcgParameters', ['initial', 'multiplyer', 'base'])

DISTRIBUTIONS_DESCRIPTION = [
    UniformDistribution(),
    GaussianDistribution(),
    ExponentialDistribution(),
    GammaDistribution(),
    TriangularDistribution(),
    SimpsonDistribution()
]

DEFAULT_LCG_PARAMS = LcgParameters(
    base=1046527,
    initial=65537,
    multiplyer=32771
)

RANDOM_VECTOR_LENGTH = 100000

def print_result(name, actual_result, reference_value_representation='', reference_value=None):
    if actual_result is not None:
        result = '{}: {}'.format(name, actual_result)
        if reference_value:
            result += ' (reference value = {}; delta: {})'.format(
                reference_value_representation + ' = ' + str(reference_value)
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
        base=read_positive_int("m"),
        initial=read_positive_int("R0"),
        multiplyer=read_positive_int("a")
    )


def lcg_demo():
    params = read_lcg_parameters()
    result = list(lcg.random_vector(RANDOM_VECTOR_LENGTH, params))
    print_result('mean', stat.mean(result), reference_value=1/2, reference_value_representation='1/2')
    print_result('variance', stat.variance(result), reference_value=1/12, reference_value_representation='1/12')
    print_result('standart deviation', stat.stdev(result))
    print_result('2K/N', lcg.uniform_ratio(result), reference_value=pi/4, reference_value_representation='pi/4')
    period = lcg.period(lambda length: lcg.random_vector(length, params))
    print_result('period', period)
    if period:
        print_result('aperiodic interval', lcg.aperiodic_interval(lambda length: lcg.random_vector(length, params), period))
    draw_histogram(result)


def print_menu():
    for i, distribution in enumerate(DISTRIBUTIONS_DESCRIPTION):
        print('\t{} : {}'.format(i+1, distribution.name))
    print('\t0 : exit')


def read_command():
    valid = False
    while not valid:
        try:
            command = int(input('>> '))
            valid = command >= 0 and command <= len(DISTRIBUTIONS_DESCRIPTION)
        except ValueError:
            print('Invalid input')
            print_menu()
    return command


def distributions_demo():
    print_menu()
    command = read_command()
    while command != 0:
        distribution = DISTRIBUTIONS_DESCRIPTION[command - 1]
        result = list(distribution.generate(RANDOM_VECTOR_LENGTH, DEFAULT_LCG_PARAMS))
        print_result('mean', stat.mean(result))
        print_result('variance', stat.variance(result))
        print_result('standart deviation', stat.stdev(result))
        draw_histogram(result)
        command = read_command()


def main():
    modes = {
        'lcg': lcg_demo,
        'dist': distributions_demo
    }
    if (len(sys.argv) == 2) and (sys.argv[1] in modes):
        command = modes[sys.argv[1]]
    else:
        print('Usage main.py dist|lcg')
        return
    command()

if __name__ == '__main__':
    main()
