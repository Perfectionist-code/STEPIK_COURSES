# Тип 24 _33196 Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите символ, который чаще всего встречается в файле сразу после буквы A.
#
# Например, в тексте ABCAABADDD после буквы A два раза стоит B, по одному разу  — A и D. Для этого текста ответом будет B.
#
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
# Моё первое решение
# import pprint
try:
    with open('24_33196.txt') as file:
        str_file = file.read()
        count = 0
        d = dict()
        for i in range(0, len(str_file) - 1):
            if str_file[i] == 'A':
                if str_file[i + 1] not in d:
                    d.setdefault(str_file[i + 1], 1)
                else:
                    count_i = d[str_file[i + 1]]
                    count_i += 1
                    d[str_file[i + 1]] = count_i
        d_to_sort = {value: key for key, value in d.items()}
        # print(sorted(d.items()), d_to_sort, sep = '\n')
        print(d_to_sort[max(d_to_sort.keys())])
        # print(sorted(d_to_sort))
        # pprint.pprint(lst_file)
except FileNotFoundError:
    print('Невозможно открыть файл')
# except:
#     print('Ошибка выполнения кода')

# s = open('24_33196.txt').readline()
# a = [s[i] for i in range(1,len(s)) if s[i-1]=='A']
# m = max([a.count(c) for c in set(a)])
# print(*[c for c in set(a) if a.count(c)==m])