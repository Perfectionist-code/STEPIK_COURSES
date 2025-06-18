from operator import add, sub


class Wallet:
    def __init__(self, currency, balance):
        self.currency = currency
        self.balance = balance

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, new_currency):
        if not isinstance(new_currency, str):
            raise TypeError('Неверный тип валюты')
        elif len(new_currency) != 3:
            raise NameError('Неверная длина названия валюты')
        elif not new_currency.isupper():
            raise ValueError('Название должно состоять только из заглавных букв')
        self.__currency = new_currency

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            raise TypeError(f'Wallet не поддерживает сравнение с {other}')
        elif other.currency != self.currency:
            raise ValueError('Нельзя сравнить разные валюты')
        return other.balance == self.balance

    def _operation(self, other, oper):
        if not isinstance(other, Wallet) or self.currency != other.currency:
            raise ValueError('Данная операция запрещена')
        return oper(self.balance, other.balance)

    def __add__(self, other):
        return Wallet(self.currency, self._operation(other, add))

    def __sub__(self, other):
        return Wallet(self.currency, self._operation(other, sub))

# wallet1 = Wallet('USD', 50)
# wallet2 = Wallet('RUB', 100)
# wallet22 = Wallet('RUB', 50)
# wallet16 = wallet2 - wallet22
# print(wallet2.balance, '-', wallet22.balance, '=', wallet16.balance )
# wallet3 = Wallet('RUB', 150)
# wallet4 = Wallet(12, 150)  # исключение TypeError('Неверный тип валюты')
# wallet5 = Wallet('qwerty', 150)  # исключение NameError('Неверная длина названия валюты')
# wallet6 = Wallet('abc', 150)  # исключение ValueError('Название должно состоять только из заглавных букв')
# print(wallet2 == wallet3)  # False
# print(wallet2 == 100)  # TypeError('Wallet не поддерживает сравнение с 100')
# print(wallet2 == wallet1)  # ValueError('Нельзя сравнить разные валюты')
# wallet7 = wallet2 + wallet3
# print(type(wallet7))
# print(wallet2.balance, '+', wallet3.balance, '=', wallet7.balance )
# print(wallet7.currency, wallet7.balance)  # печатает 'RUB 250'
# wallet2 + 45  # ValueError('Данная операция запрещена')
