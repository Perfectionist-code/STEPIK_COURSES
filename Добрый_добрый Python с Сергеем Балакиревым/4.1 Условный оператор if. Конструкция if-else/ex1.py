# Подвиг 1. На вход программе подаются два вещественных числа, записанных в одну строку через пробел. Необходимо их прочитать и вывести на экран наибольшее из этих чисел. Задачу решить с помощью условного оператора.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/4/4.1.1
#
# Sample Input:
#
# 8.7 11.0
# Sample Output:
#
# 11.0
from selectors import SelectSelector

number = list(map(float, input().split()))
if number[0] > number[1] and number[0] != number[1]:
    print(number[0])
if number[0] < number[1]:
    print(number[1])