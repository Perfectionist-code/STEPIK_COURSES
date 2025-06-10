from functools import total_ordering


@total_ordering
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return self.name

    def __lt__(self, other):
        if isinstance(other, BankAccount):
            return self.balance < other.balance
        if type(other) in (int, float):
            return self.balance < other


values = [BankAccount('Petrovich', 400), 500, BankAccount('Andrey', 200), 100, BankAccount('Zina', 150)]
values.sort()
print(*values)

values = [
    BankAccount('Petrovich', 5),
    BankAccount('Lana', 150),
    BankAccount('Petr', 150),
    BankAccount('Ivan', 10),
    BankAccount('Andrey', 3),
    BankAccount('Lena', 15),
    BankAccount('Petrov', 150)

]
values.sort(key=lambda x: (x, x.name), reverse=True)
print(*values)
