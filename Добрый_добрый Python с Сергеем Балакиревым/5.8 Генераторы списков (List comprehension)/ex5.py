# Подвиг 5. На вход программе подается натуральное число n. Необходимо его прочитать и сформировать список с помощью list comprehension, состоящий из делителей числа n (включая и само число n). Элементы полученного списка вывести в одну строчку через пробел.
#
# Ликбез: делителями числа n называются целые числа, которые делят n нацело (без остатка).
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.8.5
#
# Sample Input:
#
# 10
# Sample Output:
#
# 1 2 5 10

n = int(input())
lst = [x for x in range(1, n + 1) if n % x == 0]
print(*lst)

# n = int(input())
# mtx = [[int(i == j) for j in range(n)] for i in range(n)]
# for row in mtx:
#     print(*row)