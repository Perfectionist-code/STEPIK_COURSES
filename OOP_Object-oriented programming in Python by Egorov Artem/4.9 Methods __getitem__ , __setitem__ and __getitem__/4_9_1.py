class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return f'Vector({", ".join([str(value) for value in self.values])})'

    def __getitem__(self, item):
        if 1 <= item <= len(self.values):
            return self.values[item - 1]
        else:
            raise IndexError(f"Индекс {item} находится за пределами вектора")

# v1 = Vector(3, 655, 323, 672, 11, 6)
# print(v1[1])  # 3
# print(v1[2])  # 655
# print(v1[3])  # 323
# try:
#     print(v1[10])
# except IndexError as e:
#     print(e)
#
# v2 = Vector(10, 9, 8, 7)
# print(v2[4])
# print(v2[3])
# print(v2[2])
# print(v2[1])
# try:
#     print(v2[0])
# except IndexError as e:
#     print(e)
