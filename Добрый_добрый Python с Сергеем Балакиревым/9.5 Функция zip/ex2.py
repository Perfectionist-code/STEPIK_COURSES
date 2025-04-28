# Подвиг 2. На вход программе подается неравномерная таблица целых чисел. В программе уже реализовано считывание ее строк  и сохранение в списке lst_in:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# С помощью функции zip необходимо выравнить эту таблицу, приведя ее к прямоугольному виду, отбросив выходящие элементы в строках. Вывести результат на экран в виде такой же таблицы чисел. В конце строк при выводе пробелов быть не должно.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.5.2
#
# Sample Input:
#
# 1 2 3 4 5 6
# 3 4 5 6
# 7 8 9
# 9 7 5 3 2
# Sample Output:
#
# 1 2 3
# 3 4 5
# 7 8 9
# 9 7 5

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = ['1 2 3 4 5 6', '3 4 5 6', '7 8 9', '9 7 5 3 2']
lst_in1 = zip(*zip(*map(lambda x: list(map(int, x.split())), lst_in)))
for line in lst_in1:
    print(*line)
