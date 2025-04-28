# Подвиг 2. На вход программе подается список предметов в виде строк формата:
#
# название_1=вес_1
# ...
# название_N=вес_N
#
# В программе уже реализовано их считывание в список lst_in:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# С помощью функции map, необходимо сначала преобразовать этот список строк в кортеж, элементами которого также являются кортежи, то есть, представить список в формате:
#
# (('название_1', 'вес_1'), ..., ('название_N', 'вес_N'))
#
# А, затем, отфильтровать (исключить) все предметы с весом менее 500, используя функцию filter. Вывести на экран список оставшихся предметов (только их названия) в одну строчку через пробел в порядке их следования во входных данных.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.4.2
#
# Sample Input:
#
# зонт=1000
# палатка=10000
# спички=22
# котелок=543
# Sample Output:
#
# зонт палатка котелок

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
_tuple = tuple(map(tuple, map(lambda x: x.split('='), lst_in)))
# print(_tuple)
# print(_tuple[0])
_tuple_filtered = list(filter(lambda x: int(x[1]) >= 500, _tuple))
for i in range(len(_tuple_filtered)):
    print(_tuple_filtered[i][0], end = ' ')

# import sys
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# f = filter(lambda x: int(x[1]) >= 500, tuple(map(lambda x: tuple(x.split('=')), lst_in)))
# print(*(item for item, weight in f))

# функция filter возвращает так называемый итерируемый объект. Его можно один раз пролистать по элементам. Поскольку наши элементы это кортежи из двух значений (<название>, <вес>), то их можно сразу распаковать внутри цикла for:
#
# item for item, weight in f
# таким образом в item попадет название предмета, а в weight - его вес соотвественно.

