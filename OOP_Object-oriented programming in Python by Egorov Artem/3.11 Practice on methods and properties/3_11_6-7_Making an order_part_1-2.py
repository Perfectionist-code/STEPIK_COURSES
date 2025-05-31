class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    def deposit(self, new_deposit):
        self.__balance += new_deposit

    def is_money_enough(self, required_amount_of_money) -> bool:
        return self.__balance >= required_amount_of_money

    def payment(self, amount_to_be_debited):
        if self.is_money_enough(amount_to_be_debited):
            self.__balance -= amount_to_be_debited
        else:
            print('Не хватает средств на балансе. Пополните счет')

# billy = User('billy@rambler.ru')
# print(billy)
# print(billy.is_money_enough(350))
# billy.deposit(100)
# billy.deposit(300)
# print(billy.is_money_enough(350))
# print(billy)
# billy.payment(500)
# billy.payment(150)
# print(billy)

# jack = User('jack@gmail.ru', 800)
# print(jack)
# print(jack.balance)
# jack.payment(600)
# jack.payment(200)
# jack.payment(1)
# jack.balance = 1
# jack.payment(1)
# print(jack)