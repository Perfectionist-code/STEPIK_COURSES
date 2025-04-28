# Большой подвиг 1. Повторите быстрый алгоритм Евклида для нахождения наибольшего общего делителя двух натуральных чисел a и b. В программе необходимо объявить функцию get_nod с двумя параметрами a и b (натуральные числа) и возвращающую значение НОД(a, b).
#
# P. S. Вызывать функцию не нужно, только задать. Постарайтесь реализовать алгоритм, не возвращаясь к материалу на видео.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.3.1
#
# Sample Input:
#
# 15 121050
# Sample Output:
#
# 15

import time
def get_nod(a, b):
    """
    Функция вычисления НОД по быстрому алгоритму Евклида
    :param a: натуральное число
    :param b: натуральное число
    :return: НОД чисел a и b
    """
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b

    return a


def test_nod(func) :
    # -- тест №1 -------------------------------
    a = 28
    b = 35
    res = func(a,b)
    if res == 7 :
        print("#test1 - ok")
    else :
        print("#test1 - fail")

    # -- тест №2 -------------------------------
    a = 100
    b = 1
    res = func(a,b)
    if res == 1 :
        print("#test2 - ok")
    else :
        print("#test2 - fail")

    # -- тест №3 -------------------------------
    a = 2
    b = 10000

    st = time.time()
    res = func(a,b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1 :
        print("#test3 - ok")
    else :
        print("#test3 - fail")
    print(dt)




test_nod(get_nod)


# from math import gcd as get_nod