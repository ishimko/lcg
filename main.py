from collections import namedtuple
import statistics as stat
from math import pi

import lcg
import distributions
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
        base=int(input("m: ")),
        initial=int(input("R0: ")),
        multiplyer=int(input("a: "))
    )


def main():
    params = LcgParameters(
        base=1046527,
        initial=65537,
        multiplyer=32771
    )
    # uniform_params = distributions.UniformParameters(
    #     a=10,
    #     b=20
    # )
    # gaussian_params = distributions.GaussianParameters(
    #     mean=0,
    #     scale=1
    # )
    # exponential_params = distributions.ExponentialParameters(
    #     rate=1
    # )
    # gamma_params = distributions.GammaParameters(
    #     shape=3,
    #     scale=2
    # )
    # triangular_params = distributions.TriangularParameters(
    #     a=10,
    #     b=20
    # )
    simpson_params = distributions.SimpsonParameters(
        a=10,
        b=20
    )

#   result = list(distributions.uniform_distribution(100000, params, uniform_params))
#   result = list(distributions.gaussian_distribution(100000, params, gaussian_params))
#   result = list(distributions.exponential_distribution(100000, params, exponential_params))
#   result = list(distributions.gamma_distribution(100000, params, gamma_params))
#   result = list(distributions.triangular_distribution(100000, params, triangular_params))
    result = list(distributions.simpson_distribution(100000, params, simpson_params))
    print_result('mean', stat.mean(result), reference_value=1 / 2, reference_value_representation='1/2')
    print_result('variance', stat.variance(result), reference_value=1 / 12, reference_value_representation='1/12')
    print_result('standart deviation', stat.stdev(result))
    draw_histogram(result)


if __name__ == '__main__':
    main()
