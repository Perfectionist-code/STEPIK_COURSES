class SparseArray:
    def __init__(self, *args):
        if args:
            self.array = list(sorted(args))
        else:
            self.array = []

    def __len__(self):
        return len(self.array)

    def __getitem__(self, item):
        if item < self.__len__():
            return self.array[item]
        else:
            self.__setitem__(item)
            return self.array[item]

    def __setitem__(self, key, value=None):
        if key < (_len := self.__len__()):
            self.array[key] = value
        else:
            self.array.extend([None] * (key - _len + 1))
            self.array[key] = value

    def __delitem__(self, key):
        if key < self.__len__():
            self.array[key] = None

    @property
    def values(self):
        return tuple(self.array)


# array = SparseArray(1, 2, 3)
# print(array.values)
# print(array[7])
# print(array.values)
# array[6] = 100
# print(array.values)
# array[10] = 200
# print(array.values)
# del array[1]
# print(array.values)
# print(len(array))

# array = SparseArray()
# print(array.values)
# array[5] = 4
# array[0] = 13
# array[10] = 23
# array[5] = 81
# array[7] = 100
# print(array.values)
# print(len(array))
# print(array[20])
# print(array.values)
