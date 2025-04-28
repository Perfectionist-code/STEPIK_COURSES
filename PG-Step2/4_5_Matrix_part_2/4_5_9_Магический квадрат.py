from sympy import flatten


def is_sum_rows(matr1, n1):
    sum_row = sum(matr1[0])
    for i in range(1, n1):
        if sum_row != sum(matr1[i]):
            return False
    return sum_row


def is_sum_diagonal(*args):
    return sum([matr[i][i] for i in range(n)])


def is_true_numbers(*args):
    lst = flatten(matr)
    for i in range(1, n ** 2 + 1):
        if i not in lst:
            return False
    return True


def is_magic_square(*args):
    if not is_true_numbers(matr, n):  # Проверка условия того, что в матрице есть все числа от 1 до n^2
        return False
    sum_rows = is_sum_rows(matr, n)  # Сумма элементов в строках
    if not sum_rows:
        return False
    sum_cols = is_sum_rows([x for x in zip(*matr)], n)  # Сумма элементов в столбцах
    if not sum_cols:
        return False
    sum_main_diagonal = is_sum_diagonal(matr, n)  # Сумма элементов главной диагонали
    sum_side_diagonal = is_sum_diagonal(matr[::-1], n)  # Сумма элементов побочной диагонали

    return all([sum_side_diagonal == sum_main_diagonal, sum_main_diagonal == sum_rows, sum_rows == sum_cols])


n = int(input())
matr = [[int(x) for x in input().split()] for j in range(n)]
print(('NO', 'YES')[is_magic_square(matr, n)])
