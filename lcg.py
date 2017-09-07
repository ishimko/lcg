def get_random_vector(length, lgc_parameters):
    x = lgc_parameters.initial
    for i in range(length):
        x = (x * lgc_parameters.multiplyer) % lgc_parameters.base
        yield x/lgc_parameters.base
