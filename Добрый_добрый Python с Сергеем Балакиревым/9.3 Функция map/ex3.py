# Подвиг 3. На вход программе подается таблица целых чисел. Строки этой таблицы уже в программе читаются командой:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# Далее, используя функцию map и генератор списков, преобразуйте строки списка lst_in в двумерный (вложенный) список с именем lst2D, содержащий целые числа (а не их строковое представление). Сам список lst_in не менять.
#
# Выводить на экран ничего не нужно, только сформировать список lst2D на основе введенных данных.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.3.3
#
# Sample Input:
#
# 8 11 -5
# 3 4 10
# -1 -2 3
# 4 5 6
# Sample Output:
#
# True


import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst2D = list(map(lambda x: list(map(int, x)), map(str.split, lst_in)))
print(lst2D)

# import sys
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# # здесь продолжайте программу (используйте список lst_in)
# # переменную lst_in не менять!
# # lst2D = [*map(lambda x: [*map(int, x.split())], lst_in)]
# # lst2D = [[int(i) for i in x.split()] for x in lst_in]
# # lst2D = [*map(lambda x: [int(i) for i in x.split()], lst_in)]
# lst2D = [[*map(int, x.split())] for x in lst_in]

# import sys
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst2D = list(map(lambda x: list(map(int, x.split())), lst_in))