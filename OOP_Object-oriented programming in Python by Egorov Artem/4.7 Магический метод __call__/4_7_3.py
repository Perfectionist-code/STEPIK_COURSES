from time import perf_counter


class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        start = perf_counter()
        process = self.func()
        end = perf_counter()
        delta_time = end - start
        print(f'Время работы программы {delta_time}')
        return delta_time


@Timer
def calculate1():
    for i in range(10000000):
        2 << 99


@Timer
def calculate2():
    for i in range(10000000):
        2 ** 100


time1 = calculate1()
time2 = calculate2()
print(f'Бинарная операция выполняется в {round(time2/time1)} раз быстрее')
print(f'2 ** 100 = {2 ** 100}| 2 << 99 = {2 << 99}')
