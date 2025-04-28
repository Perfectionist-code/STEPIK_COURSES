# Подвиг 2. Объявите функцию с именем is_triangle, которая принимает три стороны треугольника (целые числа) и проверяет, можно ли из переданных аргументов составить треугольник. (Напомню, что у любого треугольника длина любой его стороны должна быть меньше суммы двух других). Если  проверка проходит, функция должна возвращать булево значение True, а иначе False.
#
# Вызывать функцию не нужно, только объявить.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.2.2
#
# Sample Input:
#
# 3 4 5
# Sample Output:
#
# True

def is_triangle(a, b, c):
    if a < b +c and b < a + c and c < a +b:
        return True
    else:
        return False


side1, side2, side3 = map(int, input().split())
print(is_triangle(side1, side2, side3))
