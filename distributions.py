from math import sqrt, log
from collections import namedtuple
import lcg

GAUSSIAN_N = 6

UniformParameters = namedtuple('UniformParameters', ['a', 'b'])
GaussianParameters = namedtuple('GaussianParameters', ['mean', 'scale'])
ExponentialParameters = namedtuple('ExponentialParameters', ['rate'])
GammaParameters = namedtuple('GammaParameters', ['shape', 'scale'])
TriangularParameters = namedtuple('TriangularParameters', ['a', 'b'])
SimpsonParameters = namedtuple('SimpsonParameters', ['a', 'b'])


def uniform_distribution(length, lgc_parameters, uniform_params):
    vector = lcg.random_vector(length, lgc_parameters)
    for x in vector:
        yield uniform_params.a + (uniform_params.b - uniform_params.a) * x


def gaussian_distribution(length, lgc_parameters, gaussian_params):
    vector = list(lcg.random_vector(length * GAUSSIAN_N, lgc_parameters))
    for x in range(0, len(vector), GAUSSIAN_N):
        yield gaussian_params.mean + gaussian_params.scale * sqrt(2) * sum((vector[x+i] - GAUSSIAN_N / 2) for i in range(0, GAUSSIAN_N))


def exponential_distribution(length, lgc_parameters, exponential_params):
    vector = lcg.random_vector(length, lgc_parameters)
    for x in vector:
        yield - (1 / exponential_params.rate) * log(x)


def gamma_distribution(length, lgc_parameters, gamma_params):
    vector = list(lcg.random_vector(length * gamma_params.shape, lgc_parameters))
    for x in range(0, len(vector), gamma_params.shape):
        yield - (1 / gamma_params.scale) * sum(log(vector[x+i]) for i in range(0, gamma_params.shape))


def triangular_distribution(length, lgc_parameters, triangular_params):
    vector = list(lcg.random_vector(length * 2, lgc_parameters))
    for x in range(0, len(vector), 2):
        yield triangular_params.a + (triangular_params.b - triangular_params.a) * max(vector[x], vector[x+1])


def simpson_distribution(length, lgc_parameters, simpson_params):
    uniform_params = UniformParameters(
        a=simpson_params.a / 2,
        b=simpson_params.b / 2
    )
    vector_a = list(uniform_distribution(length, lgc_parameters, uniform_params))
    vector_b = list(uniform_distribution(length, lgc_parameters, uniform_params))
    for i, a in enumerate(vector_a):
        yield a + vector_b[i]
