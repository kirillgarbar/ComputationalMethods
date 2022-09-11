from task_1.separate_roots import separate_roots
from task_1.reduce_roots import reduce_roots
from task_1.utils import *

if __name__ == '__main__':
    print_title()

    segments = separate_roots(f, start, end, default_steps)

    reduce_roots(f, derivative_of_f, segments, accuracy)
