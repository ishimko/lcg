from math import sqrt, log
from collections import namedtuple
import lcg
from reader import read_float, read_positive_float, read_positive_int


class UniformDistribution:
    UniformParameters = namedtuple('UniformParameters', ['a', 'b'])

    def generate(self, length, lgc_parameters, parameters=None):
        if parameters is None:
            parameters = self._read_params()
        vector = lcg.random_vector(length, lgc_parameters)
        for x in vector:
            yield parameters.a + (parameters.b - parameters.a) * x

    def _read_params(self):
        a = read_float('a')
        b = read_float('b', lambda x: x > a)
        return UniformDistribution.UniformParameters(a, b)

    @property
    def name(self):
        return 'uniform'


class GaussianDistribution:
    GaussianParameters = namedtuple('GaussianParameters', ['mean', 'scale'])
    N = 6

    def generate(self, length, lgc_parameters, parameters=None):
        if parameters is None:
            parameters = self._read_params()
        vector = list(lcg.random_vector(length * GaussianDistribution.N, lgc_parameters))
        for x in range(0, len(vector), GaussianDistribution.N):
            sub_vector = vector[x:x + GaussianDistribution.N]
            yield parameters.mean + parameters.scale * sqrt(12 / GaussianDistribution.N)*(sum(sub_vector) - GaussianDistribution.N / 2)

    def _read_params(self):
        mean = read_float('mean')
        scale = read_positive_float('scale')
        return GaussianDistribution.GaussianParameters(mean, scale)

    @property
    def name(self):
        return 'gaussian'


class ExponentialDistribution:
    ExponentialParameters = namedtuple('ExponentialParameters', ['rate'])

    def generate(self, length, lgc_parameters, parameters=None):
        if parameters is None:
            parameters = self._read_params()
        vector = lcg.random_vector(length, lgc_parameters)
        for x in vector:
            yield - (1 / parameters.rate) * log(x)

    def _read_params(self):
        rate = read_positive_float('rate')
        return ExponentialDistribution.ExponentialParameters(rate)

    @property
    def name(self):
        return 'exponential'


class GammaDistribution:
    GammaParameters = namedtuple('GammaParameters', ['shape', 'scale'])

    def generate(self, length, lgc_parameters, gamma_params=None):
        if gamma_params is None:
            gamma_params = self._read_params()
        vector = list(lcg.random_vector(length * gamma_params.shape, lgc_parameters))
        for x in range(0, len(vector), gamma_params.shape):
            yield - (1 / gamma_params.scale) * sum(log(vector[x+i]) for i in range(0, gamma_params.shape))

    def _read_params(self):
        shape = read_positive_int('shape')
        scale = read_positive_float('scale')
        return GammaDistribution.GammaParameters(shape, scale)

    @property
    def name(self):
        return 'gamma'


class TriangularDistribution:
    TriangularParameters = namedtuple('TriangularParameters', ['a', 'b'])

    def generate(self, length, lgc_parameters, triangular_params=None):
        if triangular_params is None:
            triangular_params = self._read_params()
        vector = list(lcg.random_vector(length * 2, lgc_parameters))
        for x in range(0, len(vector), 2):
            yield triangular_params.a + (triangular_params.b - triangular_params.a) * max(vector[x], vector[x+1])

    def _read_params(self):
        a = read_float('a')
        b = read_float('b', lambda x: x > a)
        return TriangularDistribution.TriangularParameters(a, b)

    @property
    def name(self):
        return 'triangle'


class SimpsonDistribution:
    SimpsonParameters = namedtuple('SimpsonParameters', ['a', 'b'])

    def generate(self, length, lgc_parameters, simpson_params=None):
        if simpson_params is None:
            simpson_params = self._read_params()
        uniform_params = UniformDistribution.UniformParameters(
            a=simpson_params.a / 2,
            b=simpson_params.b / 2
        )
        uniform_distribution = UniformDistribution()
        vector = list(uniform_distribution.generate(length*2, lgc_parameters, uniform_params))
        return map(sum, zip(vector[::2], vector[1::2]))

    def _read_params(self):
        a = read_float('a')
        b = read_float('b', lambda x: x > a)
        return SimpsonDistribution.SimpsonParameters(a, b)

    @property
    def name(self):
        return 'simpson'
