# Подвиг 3. На вход программе подается вещественное число. Необходимо его прочитать, импортировать только одну функцию floor из модуля math, вызывать ее для прочитанного числа и отобразить результат на экране.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/8/8.1.3
#
# Sample Input:
#
# 8.11
# Sample Output:
#
# 8

from math import floor
print(floor(float(input())))

# Магические методы
# print(__import__('math').ceil(float(input())))