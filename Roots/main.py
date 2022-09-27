from Roots.separate_roots import separate_roots
from Roots.reduce_roots import reduce_roots
from Roots.utils import *

if __name__ == '__main__':
    print_title()

    segments = separate_roots(f, start, end, default_steps)

    reduce_roots(f, derivative_of_f, segments, accuracy)
