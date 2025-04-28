# Подвиг 2. На вход программе подается вещественное число. Необходимо его прочитать, импортировать модуль math, вызывать функцию ceil модуля math для прочитанного числа и отобразить результат на экране.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/8/8.1.2
#
# Sample Input:
#
# 5.67
# Sample Output:
#
# 6

from math import ceil
print(ceil(float(input())))

# Магические методы
# print(__import__('math').ceil(float(input())))