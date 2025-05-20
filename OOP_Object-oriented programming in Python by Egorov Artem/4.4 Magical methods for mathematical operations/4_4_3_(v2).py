from operator import mul, add


class Vector:
    def __init__(self, *args):
        self.values = args

    def __math_operation_execute(self, func, other):
        if type(other) == int:
            return Vector(*[func(x, other) for x in self.values])
        elif isinstance(other, Vector):
            if len(self.values) == len(other.values):
                if func is add:
                    func = sum
                return Vector(*[func(x) if func is sum else func(*x) for x in zip(self.values, other.values)])
            else:
                print(f'{('Сло', 'Умно')[func is mul]}жение векторов разной длины недопустимо')
        elif type(other) not in (int, Vector):
            print(f'Вектор нельзя {('сложить', 'умножать')[func is mul]} с {other}')

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
        return self.__math_operation_execute(add, other)

    def __mul__(self, other):
        return self.__math_operation_execute(mul, other)


# v1 = Vector(1, 2, 3)
# print(v1)  # печатает "Вектор(1, 2, 3)"
#
# v2 = Vector(3, 4, 5)
# print(v2)  # печатает "Вектор(3, 4, 5)"
# v3 = v1 + v2
# print(v3)  # печатает "Вектор(4, 6, 8)"
# v4 = v3 + 5
# print(v4)  # печатает "Вектор(9, 11, 13)"
#
# v5 = v1 * 2
# print(v5)  # печатает "Вектор(2, 4, 6)"
#
# v5 + 'hi'  # печатает "Вектор нельзя сложить с hi"
#
# v3 = Vector(2, 4, 6)
# print(v3)  # печатает "Вектор(2, 4, 6)"
#
# v4 = Vector(8, 4, 1, 6)
# print(v4)  # печатает "Вектор(8, 4, 1, 6)"
#
# v3 + v4  # печатает "Сложение векторов разной длины недопустимо"
#
# v4 * v3  # печатает "Умножение векторов разной длины недопустимо"
#
# v3 * True  # печатает "Вектор нельзя умножать с True"
