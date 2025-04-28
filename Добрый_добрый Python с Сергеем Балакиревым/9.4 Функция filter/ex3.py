# Подвиг 3. На вход программе подаются целые числа, записанные через пробел. Необходимо их прочитать и оставить среди них только двузначные числа. Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.4.3
#
# Sample Input:
#
# 8 11 0 -23 140 1
# Sample Output:
#
# 11 -23
from sympy.abc import lamda

lst = list(map(int, input().split()))
lst_filtered = list(filter(lambda x: abs(x) // 10 != 0 and abs(x) // 100 == 0, lst))
print(*lst_filtered)