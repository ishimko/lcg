from collections import namedtuple
from statistics import mean, variance

from lcg import get_random_vector

LcgParameters = namedtuple('LcgParameters', ['initial', 'multiplyer', 'base'])

def minmax(data):
    iterator = iter(data)
    try:
        smallest = biggest = next(iterator)
    except StopIteration:
        raise ValueError('data is an empty sequence')
    for x in iterator:
        if x < smallest:
            smallest = x
        if x > biggest:
            biggest = x
    return smallest, biggest


def main():
    base = int(input("m: "))
    initial = int(input("R0: "))
    multiplyer = int(input("a: "))
    params = LcgParameters(multiplyer=multiplyer, initial=initial, base=base)
    result = list(get_random_vector(100000, params))
    print(mean(result))
    print(variance(result))
    print(minmax(result))

if __name__ == '__main__':
    main()
