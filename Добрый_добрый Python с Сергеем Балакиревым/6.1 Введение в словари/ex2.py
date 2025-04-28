# Подвиг 4. На вход программе поступают данные в виде набора строк в формате:
#
# ключ1=значение1
# ключ2=значение2
# ...
# ключN=значениеN
#
# Ключами здесь выступают целые числа (см. пример ниже). В программе уже реализовано считывание всех строк и сохранение их в виде списка:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# Необходимо преобразовать список lst_in в словарь d (без использования функции dict()) и вывести полученный словарь на экран командой:
#
# print(*sorted(d.items()))
# Sample Input:
#
# 5=отлично
# 4=хорошо
# 3=удовлетворительно
# Sample Output:
#
# (3, 'удовлетворительно') (4, 'хорошо') (5, 'отлично')

import sys
d_in = list(map(str.strip, sys.stdin.readlines()))
d = {}
for word in d_in:
    w = word.split(sep = '=')
    d[int(w[0])] = w[1]
print(*sorted(d.items()))


# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# d = {}
# for i in lst_in:
#     key, value = i.split('=')
#     d[int(key)] = value
# print(*sorted(d.items()))

# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst = [i.split('=') for i in lst_in]
# d = {int(i): v for i, v in lst}
# print(*sorted(d.items()))