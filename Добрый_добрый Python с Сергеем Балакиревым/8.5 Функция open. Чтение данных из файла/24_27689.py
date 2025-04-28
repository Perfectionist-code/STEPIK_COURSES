# # Тип 24 _27689 Текстовый файл состоит не более чем из 106 символов X, Y и Z. Определите максимальную длину цепочки вида XYZXYZXYZ... (составленной из фрагментов XYZ, последний фрагмент может быть неполным).
#
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.


try:
    with open('abc.txt') as file:
        trigger = 'XYZ'
        # file = open('24_27689.txt')

        string_from_file = file.read().replace('XYZ', '#')
        count_max = 0
        count_trigger = 0
        for char in string_from_file:
            if char != '#':
                count_trigger = 0
            elif char == '#':
                count_trigger += 1
                if count_max < count_trigger:
                    count_max = count_trigger
            max_len = count_max * 3
            if '#X' in string_from_file:
                max_len += 1
            elif '#XY' in string_from_file:
                max_len += 2
except FileNotFoundError:
    print('Нужный файл не найден')
        # file.close()
print(max_len)




# f = open('24_27689.txt').readline()
#
# k = mx = 0
# for i in range(len(f)):
#     if f[i-1:i+1] in 'XYZX' and k:
#         k += 1
#     elif f[i] == 'X':
#         k = 1
#     else:
#         k = 0
#     mx = max(mx, k)
# print(mx)