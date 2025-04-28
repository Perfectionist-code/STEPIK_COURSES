# Подвиг 4. На вход программе подается строка в формате:
#
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
#
# Необходимо ее прочитать и с помощью функции map преобразовать ее в кортеж tp вида:
#
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
#
# Выводить на экран ничего не нужно, только преобразовать строку в кортеж с именем tp.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.3.4
#
# Sample Input:
#
# house=дом car=машина men=человек tree=дерево
# Sample Output:
#
# True
from os.path import split

# s = input()
# s_lst = s.split()
s_lst = 'house=дом car=машина men=человек tree=дерево'.split()
print(s_lst)
# tp = tuple(tuple(x.split('=')) for x in s_lst)
# print(tp)


# s = input()
# s_lst = s.split()
tp = tuple(map(lambda x: tuple(x.split('=')), s_lst))
print(tp)