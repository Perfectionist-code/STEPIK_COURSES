# Напишите определение класса Fruit
import operator

class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __make_comparison(self, other, func):
        if isinstance(other, Fruit):
            return func(self.price, other.price)
        elif isinstance(other, (int, float)):
            return func(self.price, other)
        print(f'Объект {self.name} не может быть сравнен с {other}')

    def __eq__(self, other):
        return self.__make_comparison(other, operator.eq)

    def __lt__(self, other):
        return self.__make_comparison(other, operator.lt)

    def __gt__(self, other):
        return self.__make_comparison(other, operator.gt)

    def __le__(self, other):
        return self.__make_comparison(other, operator.le)

    def __ge__(self, other):
        return self.__make_comparison(other, operator.ge)
# Ниже код для проверки методов класса Fruit

apple = Fruit("Apple", 0.5)
orange = Fruit("Orange", 1)
banana = Fruit("Banana", 1.6)
lime = Fruit("Lime", 1.0)

assert (banana > 1.2) is True
assert (banana >= 1.2) is True
assert (banana == 1.2) is False
assert (banana != 1.2) is True
assert (banana < 1.2) is False
assert (banana <= 1.2) is False
#
assert (apple > orange) is False
assert (apple >= orange) is False
assert (apple == orange) is False
assert (apple != orange) is True
assert (apple < orange) is True
assert (apple <= orange) is True
#
assert (orange == lime) is True
assert (orange != lime) is False
assert (orange > lime) is False
assert (orange < lime) is False
assert (orange <= lime) is True
assert (orange >= lime) is True
print('Good')