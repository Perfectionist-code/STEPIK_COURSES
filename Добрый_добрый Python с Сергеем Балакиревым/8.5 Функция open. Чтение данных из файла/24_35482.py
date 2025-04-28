# Тип 24 _35482 Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт. Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
#
# Необходимо найти строку, содержащую наименьшее количество букв G (если таких строк несколько, надо взять ту, которая находится в файле раньше), и определить, какая буква встречается в этой строке чаще всего. Если таких букв несколько, надо взять ту, которая позже стоит в алфавите.
#
# Пример. Исходный файл:
#
# GIGA
#
# GABLAB
#
# AGAAA
#
# В этом примере в первой строке две буквы G, во второй и третьей  — по одной. Берём вторую строку, так как она находится в файле раньше. В этой строке чаще других встречаются буквы A и B (по два раза), выбираем букву B, так как она позже стоит в алфавите. В ответе для этого примера надо записать B.
#
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

# Моё первое решение
# import pprint
try:
    with open('24_35482.txt') as file:
        str_file = file.readlines()
        count_G_min = 10 ** 7
        lst_count = []
        for i, _str in enumerate(str_file):
            count_G = _str.count('G')
            if count_G < count_G_min:
                count_G_min = count_G
                index_min = i
        d ={}
        for char in str_file[index_min].strip('\n'):
            if char not in d:
                d.setdefault(char, 1)
            else:
                count_char = d[char]
                count_char += 1
                d[char] = count_char
        print(max(d, key = d.get))
except FileNotFoundError:
    print('Невозможно открыть файл')
# print(file.closed)
# # except:
# #     print('Ошибка выполнения кода')


# file = open("24_35482.txt", "r")
# a = [10**6]*91
# for i in range(1000):
#     st = file.readline()
#     d = [0]*91
#     for j in range(len(st)):
#         d[ord(st[j])] += 1
#     if d[71] < a[71]:
#         for k in range(len(d)):
#             a[k] = d[k]
# mx = 0
# for i in range(len(a)):
#     if a[i] >= mx:
#         mx = a[i]
#         mxchar = chr(i)
# print(mxchar)


# file = open("24_35482.txt", "r")
# dg = {'G':10**6}
# for st in file:
#     d = {}
#     for sym in st:
#         if sym in d:
#             d[sym] += 1
#         else:
#             d[sym] = 1
#     if d['G'] < dg['G']:
#         dg = d
# print(max(dg, key=dg.get))