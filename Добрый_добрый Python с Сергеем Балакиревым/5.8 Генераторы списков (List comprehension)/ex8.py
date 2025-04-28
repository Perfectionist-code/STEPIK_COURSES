# Подвиг 8. На вход программе подаются два списка целых чисел одинаковой длины, каждый с новой строки. Необходимо их прочитать и каждый сохранить в своем отдельном списке. Затем, с помощью list comprehension сформировать третий список, состоящий из суммы соответствующих пар чисел введенных списков. Элементы полученного списка вывести в одну строчку через пробел.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.8.8
#
# Sample Input:
#
# 1 2 3 4 5
# 6 7 8 9 10
# Sample Output:
#
# 7 9 11 13 15
# import sys
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]

list_in_1 = list(map(int, input().split()))
list_in_2 = list(map(int, input().split()))
lst = []
if len(list_in_1) == len(list_in_2):
    lst = [x + y for i, x in enumerate(list_in_1) for j, y in enumerate(list_in_2) if i == j]
if lst != []:
    print(*lst)


# lst_in1 = list(map(int, input().split()))
# lst_in2 = list(map(int, input().split()))
# lst = [lst_in1[i] + lst_in2[i] for i in range(len(lst_in1))]
# print(*lst)