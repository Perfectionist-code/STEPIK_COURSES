# Подвиг 6. На вход программе подается натуральное число N. Необходимо его прочитать и сгенерировать вложенный список с помощью list comprehension, размером N x N, где первая строка содержала бы все нули, вторая - все единицы, третья - все двойки и так до N-й строки. Результат вывести в виде таблицы чисел как показано в примере ниже.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.8.6
#
# Sample Input:
#
# 4
# Sample Output:
#
# 0 0 0 0
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3

n = int(input())
lst = [[x] * n for x in range(n)]
for y in lst:
    print(*y)

# n = int(input())
# mtx = [[int(i == j) for j in range(n)] for i in range(n)]
# for row in mtx:
#     print(*row)