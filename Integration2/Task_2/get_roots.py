from Roots.separate_roots import separate_roots
from Roots.reduce_roots import secant_method


def get_roots(a, b, f):
    n = 10 ** 3
    accuracy = 10 ** -12

    segments = separate_roots(f, a, b, n)

    return [root[0] for root in secant_method(f, segments, accuracy)]
