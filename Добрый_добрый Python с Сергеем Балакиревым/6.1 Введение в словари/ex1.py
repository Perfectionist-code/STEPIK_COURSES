# Подвиг 3. На вход программе подаются данные в формате ключ=значение, записанные через пробел. Значениями здесь являются целые числа (см. пример ниже). Необходимо прочитать строку с этими данными и на их основе сформировать словарь d, используя функцию dict(). Результирующий словарь вывести на экран командой:
#
# print(*sorted(d.items()))
# Sample Input:
#
# one=1 two=2 three=3
# Sample Output:
#
# ('one', 1) ('three', 3) ('two', 2)

d_in = input().split()
dict_lst = []
for word in d_in:
    word = word.split(sep = '=')
    word[-1] = int(word[-1])
    dict_lst.append(word)
    # print(word)
d = dict(dict_lst)
print(*sorted(d.items()))

# lst_in = input().split()
# lst = [[i.split('=')[0], int(i.split('=')[1])] for i in lst_in]
# d = dict(lst)
# print(*sorted(d.items()))

# d = dict(c.split('=') for c in input().split())
# for c in d:
#   d[c] = int(d[c])
# print(*sorted(d.items()))