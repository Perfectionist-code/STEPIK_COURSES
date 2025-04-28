# Подвиг 7. Используя символы малых букв латинского алфавита (строка ascii_lowercase):
#
# from string import ascii_lowercase
# запишите генератор, который бы возвращал все возможные сочетания из двух букв латинского алфавита. Выведите первые 50 сочетаний на экран в строку через пробел.
#
# Например, первые семь начальных сочетаний имеют вид:
#
# aa ab ac ad ae af ag

from string import ascii_lowercase
gen = (x + y for x in ascii_lowercase for y in ascii_lowercase)
for _ in range(50):
    print(next(gen), end = ' ')


# from string import ascii_lowercase
# gen = (i + j for i in ascii_lowercase for j in ascii_lowercase)
# [print(next(gen), end= ' ') for _ in range(50)]


# (lambda x: print(*[j + i for j in x for i in x][:50]))(__import__('string').ascii_lowercase)




