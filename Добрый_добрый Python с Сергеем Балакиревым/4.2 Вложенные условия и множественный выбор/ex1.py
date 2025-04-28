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

m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''
choice = int(input())
#m = m.splitlines()
if choice == 1:
    print(m[m.index('1'):m.index('2')-1])
elif choice == 2:
    print(m[m.index('2'):m.index('3')-1])
elif choice == 3:
    print(m[m.index('3'):m.index('4')-1])
elif choice == 4:
    print(m[m.index('4'):m.index('5')-1])
elif choice == 5:
    print(m[m.index('5'):m.index('6')-1])
else:
    print(m[m.index('6'):])