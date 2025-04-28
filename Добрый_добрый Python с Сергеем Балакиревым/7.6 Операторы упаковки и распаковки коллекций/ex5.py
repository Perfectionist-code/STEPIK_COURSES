# Подвиг 7. Объявите в программе словарь, содержащий следующие пункты меню:
#
# menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# Дополнительно на вход программе подаются еще пункты меню в виде строк в формате:
#
# название_1=url_1
# ...
# название_N=url_N
#
# В программе уже реализовано их считывание и сохранение в списке:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# Необходимо информацию из списка lst_in преобразовать в словарь того же формата, что и menu, и добавить в конец словаря menu, используя оператор распаковки для словарей. На результирующий словарь должна вести переменная menu.
#
# P.S. В программе ничего выводить на экран не нужно! Только сформировать словарь menu.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.6.7

import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_tuple = (x.split('=') for x in lst_in)
menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
d = {key: value for key, value in lst_tuple}
menu = {**menu, **d}

# здесь продолжайте программу (используйте список lst_in и menu)

print(menu)


# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# d = dict([i.split('=') for i in lst_in])
# menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# menu = dict(**menu, **d)


# import sys
# menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# menu.update([pair.split('=') for pair in map(str.strip, sys.stdin.readlines())])