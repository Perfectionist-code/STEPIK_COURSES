import time


def test_time(func) :
    def wrapper(*args,**kwargs) :
        start_time = time.time_ns()
        result = func(*args,**kwargs)
        stop_time = time.time_ns()
        working_time = stop_time - start_time
        return result,working_time

    return wrapper


@test_time
def get_nod_slow(a,b) :
    while a != b :
        if a > b :
            a -= b
        else :
            b -= a
    return a


@test_time
def get_nod_fast(a,b) :
    if a < b :
        a,b = b,a
    while b :
        a,b = b,a % b

    return a


a,b = map(int,input().split())
# get_nod_slow = test_time(get_nod_slow)
# get_nod_fast = test_time(get_nod_fast)

nod_slow,work_time_slow = get_nod_slow(a,b)
nod_fast,work_time_fast = get_nod_fast(a,b)

print(f' НОД чисел {a} и {b}: {nod_slow}. Время работы медленного алгоритма {work_time_slow} нс')
print(f' НОД чисел {a} и {b}: {nod_fast}. Время работы медленного алгоритма {work_time_fast} нс')
