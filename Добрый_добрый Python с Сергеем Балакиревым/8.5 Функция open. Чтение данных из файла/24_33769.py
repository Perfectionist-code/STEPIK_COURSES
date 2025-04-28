# Тип 24 _33769 Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите символ, который чаще всего встречается в файле после двух одинаковых символов.
#
# Например, в тексте CCCBBABAABCC есть комбинации CCC, CCB, BBA и AAB. Чаще всего  — 2 раза  — после двух одинаковых символов стоит B, в ответе для этого случая надо написать B.
#
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

# Моё первое решение
# import pprint
try:
    with open('24_33769.txt') as file:
        str_file = file.read()
        count = 0
        d = dict()
        for i in range(1, len(str_file) -1):
            if str_file[i - 1] == str_file[i]:
                if str_file[i + 1] not in d:
                    d.setdefault(str_file[i + 1], 1)
                else:
                    count_i = d[str_file[i + 1]]
                    count_i += 1
                    d[str_file[i + 1]] = count_i
        d_to_sort = {value: key for key, value in d.items()}
        print(sorted(d.items()), d_to_sort, sep = '\n')
        print(d_to_sort[max(d_to_sort.keys())])
        print(sorted(d_to_sort))
        # pprint.pprint(lst_file)
except FileNotFoundError:
    print('Невозможно открыть файл')
# except:
#     print('Ошибка выполнения кода')
