from functools import reduce
(print(f'Сумма цифр = {sum(lst := [int(x) for x in input()])}\nПроизведение цифр = {reduce(lambda a, b : a * b, lst)}'))