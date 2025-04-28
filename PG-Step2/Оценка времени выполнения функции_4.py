import timeit

test1_setup = '''
nums = list(range(100, 1000))
'''

test2_setup = '''
from collections import deque

def get_factors_fast(n):
    nsqrt = n ** .5
    factors = deque()
    if nsqrt.is_integer():
        factors.append(int(nsqrt))
    for i in range(int(nsqrt) - nsqrt.is_integer(), 0, -1):
        if n % i == 0:
            factors.appendleft(i)
            factors.append(n // i)
    return list(factors)

nums = list(range(100, 1000))
'''
code_to_test1 = '''
# тестируемый код
res = [[i for i in range(1, n // 2 + 1) if n % i == 0] + [n] for n in nums]
'''

code_to_test2 = '''
# тестируемый код
res = []
for n in nums:
    res.append(get_factors_fast(n))
'''

elapsed_time1 = timeit.repeat(stmt=code_to_test1, setup=test1_setup, number=100, repeat=5)
print(f'test1: {[round(t, 6) for t in elapsed_time1]}')
elapsed_time2 = timeit.repeat(stmt=code_to_test2, setup=test2_setup, number=100, repeat=5)
print(f'test2: {[round(t, 6) for t in elapsed_time2]}')