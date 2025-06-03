from sympy.integrals.rde import rischDE


class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return f'Vector({", ".join([str(value) for value in self.values])})'

    def __getitem__(self, item: (int, str)):
        if isinstance(item, str):
            item = len(item)
        if 1 <= item <= len(self.values):
            return self.values[item - 1]
        else:
            raise IndexError(f"Индекс {item} находится за пределами вектора")

    def __delitem__(self, key):
        # Этот вариант работает ощутимо медленнее
        # if key in self.values:
        #     self.values = list(filter(lambda x: x != key, self.values))
        # else:
        #     raise ValueError(f'Значение {key} отсутствует в векторе')

        if key in self.values:
            while key in self.values:
                self.values.remove(key)
        else:
            raise ValueError(f'Значение {key} отсутствует в векторе')

# v1 = Vector(5, 5, 5, 4, 4, 3)
# print(v1)
# del v1[4]
# print(v1)
# del v1[5]
# print(v1)
# try:
#     del v1[10]
# except ValueError as e:
#     print(e)
#
# v1 = Vector(5, 6, 7, 8, 9, 5)
# del v1[6]
# del v1[9]
# print(v1)
# del v1[5]
# print(v1)