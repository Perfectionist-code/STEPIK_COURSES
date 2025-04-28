import time
from functools import wraps
import sys


import time
from functools import wraps
import sys


def time_running_count(func):
    @wraps(func)
    def wrapper_(*args):
        start_time = time.time()
        func(args)
        end_time = time.time()
        running_time = end_time - start_time
        return running_time

    return wrapper_


@time_running_count
def range_dmitry_scherbin(*args):
    for i in range(m, n - 1, -1):
        if i % 2 != 0:
            print(i)


@time_running_count
def range_sergey(*args):
    if m % 2 == 0:
        m1 = m - 1
    else:
        m1 = m
    for i in range(m1, n - 1, -2):
        print(i)


m = 1000000
n = 1

r_d = range_dmitry_scherbin(m, n)
r_s = range_sergey(m, n)

print(f'Operating time of the range_sergey() function is {r_s}')
print(f'Operating time of the range_dmitry_scherbin() function is {r_d}')
print(f' память занимаемая range({m}, {n}, -1) равна {sys.getsizeof(range(m, n, -1))} байт')
print(f' память занимаемая range({m}, {n}, -2) равна {sys.getsizeof(range(m, n, -2))} байт')