class Vector:
    def __init__(self, *args):
        self.__args = args


    @property
    def __args(self):
        return vectorize

    @__args.setter
    def __args(self, new_args):
        self.vector = list(filter(lambda x: type(x) == int, new_args))

    def __str__(self):
        if self.vector:
            return f'Вектор{tuple(sorted(self.vector))}'
        return 'Пустой вектор'

# v1 = Vector(1, 2, 3)
# print(str(v1))
# print(isinstance(v1, Vector))
#
# v2 = Vector([4, 5], 'hello', 3, -1.5, 1, 2)
# print(str(v2))

# v3 = Vector()
# print(v3)
#
# v4 = Vector([4, 5], 'hello')
# print(str(v4))

# v5 = Vector(1, True, False, 5, 2, True, 4)
# print(str(v5))
