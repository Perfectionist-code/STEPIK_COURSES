# Подвиг 9. Необходимо объявить генератор, который бы выдавал значения функции
# f
# (
# x
# )
# =
# 1
# 2
# ⋅
# x
# 2
# −
# 2
# f(x)=
# 2
# 1
# ​
#  ⋅x
# 2
#  −2 для аргумента x в диапазоне [a; b] (включительно) с шагом 0.01. Целые числа a, b (a< b) подаются на вход программе в одну строчку через пробел. Нужно их прочитать и через генератор вывести на экран первые 20 значений функции с точностью до сотых.
#
# P.S. Значения функции в генераторе вычислять командой:
#
# f(x) = 0.5 * pow(x, 2) - 2.0
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.1.9
#
# Sample Input:
#
# 0 10
# Sample Output:
#
# -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -1.99 -1.99 -1.99 -1.99 -1.99 -1.99 -1.99 -1.98 -1.98

a, b = map(int, input().split())

gen = (round((0.5 * (0.01 * x * x /100) - 2.0), 2) for x in range(a*100,b * 100 + 1))
for _ in range(20):
    print(next(gen), end = ' ')


# a, b = map(int, input().split())
# gen = (round(0.5 * pow(x/100, 2) - 2.0, 2) for x in range(a*100, b*100+1))
# print(*list(gen)[:20])

# import numpy as np
# a, b = map(float,input().split())
# gen = (x for x in np.arange(a, b+0.01, 0.01))
# for i, x in enumerate(gen):
#     print(round(0.5 * pow(x, 2) - 2.0, 2), end=' ') if i < 20 else ''
