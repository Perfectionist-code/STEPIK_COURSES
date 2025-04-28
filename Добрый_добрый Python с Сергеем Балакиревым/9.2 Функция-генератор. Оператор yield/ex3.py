# Подвиг 3. На вход программе подается натуральное число N (N > 8). Необходимо его прочитать и объявить функцию-генератор, которая бы выдавала пароль длиной N символов из случайных букв, цифр и некоторых других знаков. Значение N передается в функцию-генератор первым аргументом. Для получения последовательности допустимых символов для генерации паролей в программе импортированы две строки: ascii_lowercase, ascii_uppercase (см. листинг ниже), на основе которых формируется общий список:
#
# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
# Функция-генератор должна при каждом вызове возвращать новый пароль из случайно выбранных символов chars длиной N и делать это бесконечно, то есть, вызывать ее можно бесконечное число раз.
#
# Сгенерируйте с помощью функции-генератора первые пять паролей и выведите их в столбик (каждый с новой строки).
#
# Подсказка: сгенерировать случайный индекс indx в диапазоне [a; b] для выбора символа из chars можно с помощью функции randint модуля random:
#
# import random
# random.seed(1)
# indx = random.randint(a, b)
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.2.3
#
# Sample Input:
#
# 10
# Sample Output:
#
# riGp?58WAm
# !dX3a5IDnO
# dcdbWB2d*C
# 4?DSDC6Lc1
# mxLpQ@2@yM


# put your python code here
# from string import ascii_lowercase, ascii_uppercase
# import random
#
#
# def generate_password(N):
#     chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
#     chars_length = len(chars)
#     while True:
#         password = ''
#         # Данный блок создаёт генератор пароля
#         for _ in range(N):
#             indx = random.randint(0, chars_length - 1)
#             password += chars[indx]
#
#         yield password
#
#
# length_password = int(input())
# random.seed(1)
# passw = generate_password(length_password)
# for _ in range(5):
#     print(next(passw))

from random import seed, randint
from string import ascii_lowercase, ascii_uppercase

def pass_generate(N):
    for _ in range(N): yield chars[randint(0, len(chars))]


N = int(input())
seed(1)
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
[print(*pass_generate(N), sep='') for _ in range(5)]
