class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return f'Vector({", ".join([str(value) for value in self.values])})'

    def __getitem__(self, item):
        if cnt := self.values.count(item):
            if cnt == 1:
                return self.values.index(item) + 1
            else:
                return [i for i, x in enumerate(self.values, 1) if x == item]
        else:
            raise ValueError(f'В векторе отсутствует значение {item}')

# v1 = Vector(3, 655, 323, 672, 11, 6)
# print(v1[655])  # 2
# print(v1[672])  # 4
# print(v1[3])  # 1
# try:
#     print(v1[10])
# except ValueError as e:
#     print(e)
#
# v1 = Vector(5, 5, 5, 4, 4, 3)
# print(v1[4])  # [4, 5]
# print(v1[5])  # [1, 2, 3]
# print(v1[3])  # 6
# try:
#     print(v1[2])
# except ValueError as e:
#     print(e)
