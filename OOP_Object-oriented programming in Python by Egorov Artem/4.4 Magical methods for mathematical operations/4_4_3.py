from operator import mul


class Vector:
    def __init__(self, *args):
        self.values = args

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, new_args):
        self.__values = sorted(filter(lambda x: type(x) == int, new_args))

    def __str__(self):
        if self.values:
            return f'Вектор{tuple(self.values)}'
        return 'Пустой вектор'

    def __add__(self, other):
        if type(other) == int:
            return Vector(*[x + other for x in self.values])
        elif isinstance(other, Vector) and len(self.values) == len(other.values):
            return Vector(*[sum(x) for x in zip(self.values, other.values)])
        elif type(other) not in (int, Vector):
            print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        if type(other) == int:
            return Vector(*[x * other for x in self.values])
        elif isinstance(other, Vector) and len(self.values) == len(other.values):
            return Vector(*[mul(*x) for x in zip(self.values, other.values)])
        elif type(other) not in (int, Vector):
            print(f'Вектор нельзя умножать с {other}')

# v1 = Vector(1,2,3)
# print(v1) # печатает "Вектор(1, 2, 3)"
#
# v2 = Vector(3,4,5)
# print(v2) # печатает "Вектор(3, 4, 5)"
# v3 = v1 + v2
# print(v3) # печатает "Вектор(4, 6, 8)"
# v4 = v3 + 5
# print(v4) # печатает "Вектор(9, 11, 13)"
#
# v5 = v1 * 2
# print(v5) # печатает "Вектор(2, 4, 6)"
#
# v5 + 'hi' # печатает "Вектор нельзя сложить с hi"
