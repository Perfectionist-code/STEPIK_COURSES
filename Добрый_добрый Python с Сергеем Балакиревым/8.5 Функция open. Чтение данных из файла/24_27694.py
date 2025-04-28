# Тип 24 _27694 Текстовый файл состоит не более чем из 106 символов A, B и C. Определите максимальную длину цепочки вида ABABAB... (составленной из фрагментов AB, последний фрагмент может быть неполным).
#
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

# Моё первое решение
try:
    with open('24_27694.txt') as file:
        str_file = file.read().replace('C', ' ')
        while 'AA' in str_file:
            str_file = str_file.replace('AA', 'A A')
        while 'BB' in str_file:
            str_file = str_file.replace('BB', 'B B')
        lst_set = {x if x[0] == 'A' else x.lstrip('B') for x in str_file.split()}
        print(sorted(lst_set, key = len, reverse = True))
        file.close()
        print(len(max(lst_set, key = len)))
except FileNotFoundError:
    print('Невозможно открыть файл')
except:
    print('Ошибка выполнения кода')

