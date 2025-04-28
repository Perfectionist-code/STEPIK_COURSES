# Подвиг 2. На вход программе поступают строки в формате:
#
# предмет_1=вес_1
# ...
# предмет_N=вес_N
#
# Веса предметов заданы целыми числами. В программе уже реализовано их считывание в список lst_in:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# Необходимо на основе этих данных сформировать словарь (ключи - названия предметов, значения - вес предметов) и, затем, на основе этого словаря сформировать список предметов по убыванию их веса. (В списке должны находиться только наименования предметов без их весов).
#
# Отобразить полученный список в виде строки с названиями через пробел.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.7.2
#
# Sample Input:
#
# ножницы=100
# котелок=500
# спички=20
# зажигалка=40
# зеркальце=50
# Sample Output:
#
# котелок ножницы зеркальце зажигалка спички


import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = [
#           'ножницы=100',
#           'котелок=500',
#           'спички=20',
#           'зажигалка=40',
#           'зеркальце=50'
#          ]

d = {key: int(value) for key, value in (map(lambda x: x.split('='), lst_in))}
print(*list(dict(sorted(d.items(), key = lambda x: x[1], reverse = True))))



# d = dict((c.split('=') for c in open(0)))
# print(*sorted(d, key=lambda x: int(d[x]), reverse=True))


# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# d = {k: int(v) for k, v in (line.split('=') for line in lst_in)}
# print(*sorted(d, key=d.get, reverse=True))

# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# d = {i: int(j) for i, j in [k.split('=') for k in lst_in]}
# lst = [i[0] for i in sorted(d.items(), key=lambda x: -x[1])]
# print(*lst)