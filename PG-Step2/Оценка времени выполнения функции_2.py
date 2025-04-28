import collections
import time
from functools import wraps
import sys
from collections import Counter

def time_running_count(func):
    @wraps(func)
    def wrapper_(*args):
        start_time = time.time_ns()
        func(args)
        end_time = time.time_ns()
        running_time = end_time - start_time
        return running_time

    return wrapper_


@time_running_count
def function_with_set(*args):
    return max(set(_str[::-1]), key = _str.count)


@time_running_count
def function_without_set_1(*args):
    return max(_str[::-1], key = lambda x: [_str.count(x)])

# @time_running_count
# def function_without_set_2(*args):
#     return max(_str[::-1], key = _str.count)

@time_running_count
def function_without_set_2(*args):
    return max(_str[::-1], key = Counter(_str).get)


@time_running_count
def function_collection_counter(*args):
    return collections.Counter(_str).most_common(1)[0][0]



_str = 'afgdsfdfffffffffffffffffffffffffgggggggggggппппппппппппппппппккккккккккккккккккккккккоооооооооооооооооооьитронггггпппорцццццццццццццццццццwwwwwwwwwwwwwwwwwwwwwwwwwgggggggggggggghhhhhhhhhhhhhhhhhhhhhhhtttttrfffggggggggggggeeeeeeeeeeee'
f_w_s = function_with_set(_str)
f_wo_s_1 = function_without_set_1(_str)
f_wo_s_2 = function_without_set_2(_str)
f_c_c = function_collection_counter(_str)
print(f'Operating time of the function_with_set() function is {f_w_s} нс')
print(f'Operating time of the function_without_set_1() function is {f_wo_s_1} нс')
print(f'Operating time of the function_without_set_2() function is {f_wo_s_2} нс')
print(f'Operating time of the function_collection_counter() function is {f_c_c} нс')




