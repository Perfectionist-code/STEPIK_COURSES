# Большой подвиг 5. (Для закрепления предыдущего материала). На вход программе подается таблица целых чисел (см. пример ниже) размером N x N элементов (N определяется по входным данным). Необходимо прочитать эти числа и сохранить в виде двумерного (вложенного) списка lst2D размером N x N элементов. Полученная таблица будет содержать нули и кое-где единицы. С помощью функции с именем verify, на вход которой подается двумерный список чисел (первый параметр), необходимо проверить, являются ли единицы изолированными друг от друга, то есть, вокруг каждой единицы должны быть нули.
#
# Рекомендуется следующий алгоритм. В функции verify производить перебор двумерного списка. Для каждого элемента (списка) со значением 1 вызывать еще одну вспомогательную функцию is_isolate для проверки изолированности единицы. То есть, функция is_isolate должна возвращать True, если единица изолирована и False в противном случае.
#
# Как только встречается не изолированная единица, функция verify должна возвращать False. Если успешно доходим (по элементам списка) до конца, то возвращается значение True.
#
# Функцию verify выполнять не нужно, только объявить.
#
# P. S. При реализации функции is_isolate не следует прописывать восемь операторов if. Подумайте, как это можно сделать красивее (с точки зрения реализации алгоритма).
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.5.5
#
# Sample Input:
#
# 1 0 0 0 0
# 0 0 1 0 0
# 0 0 0 0 0
# 0 1 0 1 0
# 0 0 0 0 0
# Sample Output:
#
# True

# import sys
#
#
# def is_isolate(*args,i,j) :
#     summa = 0
#     for k in range(0,2) :
#         summa += args[i][j + k] + args[i + 1][j + k]
#     if summa <= 1 :
#         return True
#     else :
#         return False
#
#
# def verify(*args) :
#     print(args)
#     n = len(args)
#     for x in range(n - 1) :
#         for y in range(len(args[x]) - 1) :
#             if not is_isolate(*args,i = x,j = y) :
#                 return False
#     return True
#
#
# lines = sys.stdin.readlines()
# lst2D = [[int(y) for y in x.split()] for x in lines]
# print(verify(*lst2D))
# print(lst2D)
# print(*lst2D)

import sys


def is_isolate(*args,i,j) :
    # print(*(args))
    summa = 0
    for k in range(0,2) :
        summa += args[i][j + k] + args[i + 1][j + k]
    if summa <= 1 :
        return True
    else :
        return False


def verify(*args) :
    args = list(*args)
    # print(args)
    n = len(args)
    for x in range(n - 1) :
        for y in range(len(args[x]) - 1) :
            if not is_isolate(*args,i = x,j = y) :
                return False
    return True

lines = sys.stdin.readlines()
lst2D = [[int(y) for y in x.split()] for x in lines]
print(verify(lst2D))
#
#
# def is_isolate(*args):
#     return sum(*args) < 2
#
#
# def verify(lst):
#     size = len(lst)
#     return False not in [is_isolate(lst[i][j:j+2] + lst[i+1][j:j+2])
#                          for j in range(size - 1)
#                          for i in range(size - 1)]