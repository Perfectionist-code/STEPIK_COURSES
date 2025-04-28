# Подвиг 3. На вход программе подается таблица целых чисел. В программе уже реализовано считывание ее строк  и сохранение в списке lst_in:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# Необходимо сначала список строк lst_in представить двумерным (вложенным) списком чисел, а затем, с помощью функции zip выполнить транспонирование этой таблицы (то есть, строки заменить на соответствующие столбцы). Результат вывести на экран в виде таблицы чисел (числа в строках следуют через пробел). В конце строк при выводе пробелов быть не должно.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.5.3
#
# Sample Input:
#
# 1 2 3 4
# 5 6 7 8
# 9 8 7 6
# Sample Output:
#
# 1 5 9
# 2 6 8
# 3 7 7
# 4 8 6

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in1 = list(zip(*list(map(lambda x: list(map(int, x.split())), lst_in))))
for line in lst_in1:
    print(*line)


# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst = [list(map(int, i.split())) for i in lst_in]
# for i in zip(*lst):
#     print(*i)