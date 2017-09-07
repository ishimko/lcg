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


def get_uniform_ratio(numbers):
    pairs = ((numbers[i], numbers[i+1]) for i in range(0, len(numbers), 2))
    K = sum(1 for x1, x2 in pairs if x1**2 + x2**2 < 1)
    return 2*K / len(numbers)


def get_random_vector(length, lgc_parameters):
    x = lgc_parameters.initial
    for i in range(length):
        x = (x * lgc_parameters.multiplyer) % lgc_parameters.base
        yield x/lgc_parameters.base
