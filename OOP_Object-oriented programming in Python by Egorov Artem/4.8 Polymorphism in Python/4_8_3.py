class DateUSA:
    def __init__(self, date, month, year):
        self.date, self.month, self.year = date, month, year

    def format(self):
        return f'{self.month:02d}/{self.date:02d}/{self.year:04d}'

    def isoformat(self):
        return f'{self.year:04d}-{self.month:02d}-{self.date:02d}'


class DateEurope:
    def __init__(self, date, month, year):
        self.date, self.month, self.year = date, month, year

    def format(self):
        return f'{self.date:02d}/{self.month:02d}/{self.year:04d}'

    def isoformat(self):
        return f'{self.year:04d}-{self.month:02d}-{self.date:02d}'


# d = DateEurope(5, 12, 2001)
# print(d.format())
# print(d.isoformat())
#
# d = DateUSA(1, 5, 890)
# print(d.format())
# print(d.isoformat())
#
# dates = [
#     DateUSA(1, 2, 2024),
#     DateUSA(2, 2, 2024),
#     DateEurope(20, 9, 2024),
#     DateEurope(17, 12, 2024),
#     DateUSA(3, 2, 2022),
#     DateEurope(14, 3, 2001),
# ]
# for d in dates:
#     print(d.format())
#     print(d.isoformat())
#     print('-' * 10)