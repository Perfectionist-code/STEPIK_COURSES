from collections import defaultdict


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
            return True
        else:
            print('Не хватает средств на балансе. Пополните счет')
            return False


class Cart:
    def __init__(self, user):
        self.__user = user
        self.goods = defaultdict(int)
        self.__total = 0

    @property
    def __user(self):
        return self.user

    @__user.setter
    def __user(self, new_user):
        if isinstance(new_user, User):
            self.user = new_user

    def add(self, product, quantity=1):
        if isinstance(product, Product):
            self.goods[product] += quantity
            self.__total += quantity * product.price


    def remove(self, product, quantity=1):
        if isinstance(product, Product):
            quantity = min(quantity, self.goods[product])
            self.goods[product] -= quantity
            self.__total -= quantity * product.price
            if self.goods[product] == 0:
                del self.goods[product]

    @property
    def total(self):
        return self.__total

    def order(self):
        print(('Проблема с оплатой', 'Заказ оплачен')[self.user.payment(self.__total)])

    def print_check(self):
        print('---Your check---')
        for item in sorted(self.goods, key=lambda x: x.name):
            print(item.name, item.price, self.goods[item], item.price * self.goods[item])
        print(f'---Total: {self.total}---')

billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user)  # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total)  # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order()  # Заказ оплачен
print(cart_billy.user.balance)  # 20