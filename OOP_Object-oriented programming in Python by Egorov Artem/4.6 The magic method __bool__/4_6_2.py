# Напишите определение класса Quadrilateral
class Quadrilateral:

    def __init__(self, *args):
        self.length, *self.width = args

    def __str__(self):
        if self.width:
            return f'Прямоугольник размером {self.length}х{self.width[0]}'
        return f'Квадрат размером {self.length}х{self.length}'

    def __bool__(self):
        return not self.width


# Ниже код для проверки методов класса City

# q1 = Quadrilateral(10)
# print(q1)
# print(bool(q1))
# print(isinstance(q1, Quadrilateral))
#
# q2 = Quadrilateral(3, 5)
# print(q2)
# print(bool(q2))
#
# q3 = Quadrilateral(4, 7)
# print(q3)
# print(bool(q3))
