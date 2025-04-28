# Значимый подвиг 4. Имеется таблица с данными, представленная в формате:
#
# Номер;Имя;Оценка;Зачет
# 1;Иванов;3;Да
# 2;Петров;2;Нет
# ...
# N;Балакирев;4;Да
#
#  В программе уже реализовано их считывание в список lst_in:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# Данные этого списка необходимо разбить по разделителю ";" и представить в виде двумерного (вложенного) кортежа в формате:
#
# ( ('Номер', 'Имя', 'Оценка', 'Зачет'), (1, 'Иванов', 3, 'Да'), (2, 'Петров', 2, 'Нет'), ... )
#
# При этом все числа должны быть представлены как целые числа. Затем, отсортировать этот кортеж так, чтобы столбцы шли в порядке:
#
# Имя;Зачет;Оценка;Номер
#
# Реализовать эту операцию с помощью сортировки. Результат должен быть представлен также в виде двумерного кортежа и присвоен переменной с именем t_sorted.
#
# Программа ничего не должна выводить на экран, только формировать двумерный кортеж с переменной t_sorted.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.7.4
#
# Sample Input:
#
# Номер;Имя;Оценка;Зачет
# 1;Портос;5;Да
# 2;Арамис;3;Да
# 3;Атос;4;Да
# 4;д'Артаньян;2;Нет
# 5;Балакирев;1;Нет
# Sample Output:
#
# True


import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = [
#           'Номер;Имя;Оценка;Зачет',
#           '1;Портос;5;Да',
#           '2;Арамис;3;Да',
#           '3;Атос;4;Да',
#           '4;д\'Артаньян;2;Нет',
#           '5;Балакирев;1;Нет'
#
#          ]
lst_tp = tuple((int(n) if n.isdigit() else n, y, int(m) if m.isdigit() else m, z) for n, y, m, z in map(lambda x: x.split(';'), lst_in))
t_sorted = tuple([(x[1], x[3], x[2], x[0]) for x in lst_tp])
print(t_sorted)


# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# haders = tuple('Имя;Зачет;Оценка;Номер'.split(';'))
# t = tuple(tuple(int(e) if e.isdigit() else e for e in s.split(';')) for s in lst_in)
# t_sorted = tuple(zip(*sorted(zip(*t), key=lambda x: haders.index(x[0]))))


# import sys

# lst_in = list(map(str.strip, sys.stdin.readlines()))

# order = "Имя;Зачет;Оценка;Номер"
# t = tuple(tuple(int(st) if st.isdigit() else st for st in row.split(";")) for row in lst_in)
# t_sorted = tuple(zip(*sorted(list(zip(*t)), key=lambda x: order.find(x[0]))))