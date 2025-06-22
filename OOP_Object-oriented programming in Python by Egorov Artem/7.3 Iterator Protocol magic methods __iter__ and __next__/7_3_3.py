# Напишите определение класса PowerTwo
class PowerTwo:
    def __init__(self, power: int):
        self.power_end = power
        self.power = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.power <= self.power_end:
            p = self.power
            self.power += 1
            return 1 << p
        else:
            self.power = 0
            raise StopIteration


# Ниже код для проверки методов класса PowerTwo

numbers = PowerTwo(2)

assert hasattr(numbers, '__next__') is True
assert hasattr(numbers, '__iter__') is True

iterator = iter(numbers)
print('Элементы итератора PowerTwo(2)')
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
    raise ValueError('Не реализовали StopIteration')
except StopIteration:
    pass

print('-' * 15)
print('Элементы итератора PowerTwo(20)')
for i in PowerTwo(20):
    print(i)
