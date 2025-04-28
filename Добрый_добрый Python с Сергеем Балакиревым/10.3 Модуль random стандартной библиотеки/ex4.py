# Подвиг 5. На вход программе подается таблица целых чисел, записанных через пробел. В программе уже реализовано чтение ее строк:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# Необходимо преобразовать список строк lst_in в двумерный список чисел. Затем, в полученном списке (таблице) перемешать столбцы, используя функции shuffle и zip. Результат вывести на экран (также в виде таблицы). При выводе в конце строк не должно быть пробелов.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/10/10.3.5
#
# Sample Input:
#
# 1 2 3 4
# 5 6 7 8
# 9 8 6 7
# Sample Output:
#
# 4 1 3 2
# 8 5 7 6
# 7 9 6 8

import sys
import random
random.seed(1)
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst = [x for x in map(lambda x: [int(y) for y in x.split()], lst_in)]
# lst = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 6, 7]]
lst_1 = list(zip(*lst))
random.shuffle(lst_1)
for i in zip(*lst_1):
    print(*i)


# import sys
# import random as rnd
#
# columns = list(zip(*map(str.split, sys.stdin)))
# rnd.seed(1)
# rnd.shuffle(columns)
# for row in zip(*columns):
#     print(*row)

# import sys
# import random
# random.seed(1)
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst = list(zip(*map(str.split, lst_in)))
# random.shuffle(lst)
# [print(*i) for i in zip(*lst)]