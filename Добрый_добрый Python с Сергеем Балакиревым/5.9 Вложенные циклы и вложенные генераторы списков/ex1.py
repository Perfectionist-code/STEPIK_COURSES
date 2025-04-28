# Подвиг 1. На вход программе подается двумерная таблица из целых чисел (см. пример ниже). В программе уже реализовано его чтение и сохранение в двумерном списке:
#
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
# С помощью list comprehension необходимо преобразовать двумерный список lst_in в одномерный так, чтобы значения элементов шли в обратном порядке. Результат отобразить в виде строки из чисел, записанных через пробел.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.9.1
#
# Sample Input:
#
# 1 2 3 4
# 5 6 7 8
# 9 8 7 6
# 5 4 3 2
# Sample Output:
#
# 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1

import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
lst = [x
       for row in lst_in[::-1]
       for x in row[::-1]]
print(*lst)