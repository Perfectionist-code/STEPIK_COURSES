# Подвиг 5. Из модуля random импортируйте только две функции: seed и randint. Затем, в программе выполните их следующим образом:
#
# seed(1)
# print(randint(10, 50))

from random import seed, random as rnd
seed(10)
print(round(rnd(), 2))


# __import__('random').seed(1)
# print(__import__('random').randint(10,50))pip