from functools import lru_cache
from time import time
from functools import wraps

def time_running_count(func):
    @wraps(func)
    def wrapper_(*args):
        start_time = time()
        func()
        end_time = time()
        running_time = end_time - start_time
        return running_time

    return wrapper_


@lru_cache(2000)
def f(n):
    if n == 0: return 6
    if n > 0 and not n % 2: return 1 + f(n // 2)
    return f(n // 2)

@time_running_count
def program_1():
    cnt = 0
    for i in range(1, 1_000_000_001):
        if (d:=f(i)) == 9:
            cnt += 1
    print(cnt)

running_time = program_1()
print(running_time)



