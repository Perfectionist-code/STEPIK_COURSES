# Тип 24 _27690 Текстовый файл состоит не более чем из 106 символов A, B и C. Определите максимальное количество идущих подряд символов A.
#
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

# Моё первое решение
# file = open('24_27690.txt')
# count = 1
# string_from_file = file.read()
# count_max = 0
# # count_trigger = 0
# for i in range(1, len(string_from_file)):
#     if string_from_file[i - 1] != string_from_file[i]:
#         count += 1
#     elif count_max < count:
#         count_max = count
#         count = 1
#     else:
#         count = 1
# file.close()
# print(count_max)

# Моё второе решение
file = open('24_27690.txt')
lst_file = file.read().replace('AA', 'A A').replace('BB', 'B B').replace('CC', 'C C').split()
lst_set = {x for x in lst_file}
file.close()
print(len(max(lst_set, key = len)))


# f = open('24_27690.txt').readline()
# while 'AA' in f or 'BB' in f or 'CC' in f:
#     f = f.replace('AA','A A')
#     f = f.replace('BB','B B')
#     f = f.replace('CC','C C')
# f = f.split()
# print(max(len(x) for x in f))


# f = open('24_27690.txt').readline()
# k = 1
# m = 0
# for i in range(1, len(f)):
#     if f[i] != f[i-1]:
#         k += 1
#     else:
#         m = max(m, k)
#         k = 1
# m = max(m, k)
# print(m)
