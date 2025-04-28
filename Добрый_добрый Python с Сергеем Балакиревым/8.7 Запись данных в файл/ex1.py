# Подвиг 2. Имеется фрагмент программы (см. листинг ниже). При его выполнении возникает ошибка FileNotFoundError. Запишите конструкцию try / except, чтобы отображалось сообщение "File Not Found", если файл не удается открыть.
import random
from random import choice

try:
    with open("abc.txt", 'w') as file:
        gen_type = ['X', 'Y', 'Z']
        for i in range(10 ** 6 + 1):
            file.write(choice(gen_type))
except FileNotFoundError:
    print('File Not Found')
