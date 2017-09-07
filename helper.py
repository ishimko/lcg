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