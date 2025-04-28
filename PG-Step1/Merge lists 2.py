# объявление функции
def is_valid_triangle(side1, side2, side3):
    return side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))