# Подвиг 5. Объявите класс TriangleChecker, объекты которого можно было бы создавать командой:
#
# tr = TriangleChecker(a, b, c)
#
# Здесь a, b, c - длины сторон треугольника.
#
# В классе TriangleChecker необходимо объявить метод is_triangle(), который бы возвращал следующие коды:
#
# 1 - если хотя бы одна сторона не число (не float или int) или хотя бы одно число меньше или равно нулю;
# 2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
# 3 - стороны a, b, c образуют треугольник.
#
# Проверку параметров a, b, c проводить именно в таком порядке.
#
# Прочитайте из входного потока строку, содержащую три числа, разделенных пробелами, командой:
#
# a, b, c = map(int, input().split())
#
# Затем, создайте объект tr класса TriangleChecker и передайте ему прочитанные значения a, b, c. Вызовите метод is_triangle() из объекта tr и выведите результат на экран (код, который она вернет).
#
# Sample Input:
#
# 3 4 5
#
# Sample Output:
#
# 3

class TriangleChecker:

    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def _isinstance(self, side):
        return (type(side) in (int, float)) and side > 0

    def is_triangle(self):
        if not all([tr._isinstance(self.side_a),
                    tr._isinstance(self.side_b),
                    tr._isinstance(self.side_c)]):
            return 1
        a = self.side_a
        b = self.side_b
        c = self.side_c
        if all([a + b > c, a + c > b, c + b > a]):
            return 3
        else:
            return 2


a, b, c = map(int, input().split())  # эту строчку не менять
# здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle() с выводом информации на экран

tr = TriangleChecker(a, b, c)
# tr = TriangleChecker(True, True, True)
print(tr.is_triangle())
