from collections import namedtuple
import statistics as stat
from math import pi
import sys

import lcg
import distributions
from distributions import Distributions
from histogram import draw_histogram


LcgParameters = namedtuple('LcgParameters', ['initial', 'multiplyer', 'base'])


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
        base=read_positive("m"),
        initial=read_positive("R0"),
        multiplyer=read_positive("a")
    )


def read_positive(name):
    result = None
    while (result is None) or (result <= 0):
        try:
            result = int(input('{}: '.format(name)))
        except ValueError:
            print('Invalid input, positive integer is required')
    return result


def lcg_demo():
    params = read_lcg_parameters()
    result = list(lcg.random_vector(100000, params))
    print_result('mean', stat.mean(result), reference_value=1/2, reference_value_representation='1/2')
    print_result('variance', stat.variance(result), reference_value=1/12, reference_value_representation='1/12')
    print_result('standart deviation', stat.stdev(result))
    print_result('2K/N', lcg.uniform_ratio(result), reference_value=pi/4, reference_value_representation='pi/4')
    period = lcg.period(lambda length: lcg.random_vector(length, params))
    print_result('period', period)
    if period:
        print_result('aperiodic interval', lcg.aperiodic_interval(lambda length: lcg.random_vector(length, params), period))
    draw_histogram(result)


def print_menu(distributions_description):
    print('\t0 : exit')
    for i, distribution in enumerate(distributions_description):
        print('\t{} : {}'.format(i+1, distribution.name))


def read_command(maximum):
    valid = False
    while not valid:
        try:
            command = int(input('>> '))
            valid = command >= 0 and command <= maximum
        except ValueError:
            print('Invalid input')
    return command


def distributions_demo():
    distributions_labels = [
        Distributions.uniform,
        Distributions.gaussian,
        Distributions.exponential,
        Distributions.gamma,
        Distributions.triangular,
        Distributions.simpson
    ]
    params = LcgParameters(
        base=1046527,
        initial=65537,
        multiplyer=32771
    )

    print_menu(distributions_labels)
    command = read_command(len(distributions_labels))
    while command != 0:
        distribution = distributions_labels[command - 1]
        distribution_params = distribution.parameters_reader()
        result = list(distribution.generator(100000, params, distribution_params))
        print_result('mean', stat.mean(result))
        print_result('variance', stat.variance(result))
        print_result('standart deviation', stat.stdev(result))
        draw_histogram(result)
        command = read_command(len(distributions_labels))


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
