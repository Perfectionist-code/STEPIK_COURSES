# Подвиг 2. На вход программе подаются целые числа, записанные через пробел. Необходимо их прочитать и с помощью list comprehension сформировать двумерный список lst размером N x N (квадратную таблицу чисел). Гарантируется, что из набора введенных чисел можно сформировать квадратную матрицу (таблицу). Полученный двумерный список отобразить командой:
#
# print(lst)
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.9.2
#
# Sample Input:
#
# 1 2 3 4 5 6 7 8 9
# Sample Output:
#
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
from os import lstat

list_in = [int(x) for x in input().split()]
N = int(len(list_in) ** 0.5)
if len(list_in) % int(len(list_in) ** 0.5) == 0 :
       lst = [list_in[i * N :i * N + N]
              for i in range(N)
              ]
       print(lst)
else:
       print(f'Вы ввели {len(list_in)} чисел. Из них не возможно построить квадратную матрицу')

# Красивое решение
# l = list(map(int, input().split()))
# n = int(len(l)**0.5)
# it = iter(l)
# m = [[next(it) for y in range(n)] for x in range(n)]
#
# print(m)