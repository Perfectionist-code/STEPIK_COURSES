class Date:

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_str(cls, date_str: str):
        day, month, year = map(int, date_str.split('-'))
        # print(day, month, year)
        return cls(day, month, year)


# day_1 = Date(20, 9, 1997)
# print(day_1.day)
# print(day_1.month)
# print(day_1.year)
#
# day_2 = Date(1, 2, 2003)
# print(day_2.day, day_2.month, day_2.year)

# ------------------------------------

# day_1 = Date.from_str('12-4-2024')
# day_2 = Date.from_str('06-09-2022')
# print(day_1.day, day_1.month, day_1.year)
# print(day_2.day, day_2.month, day_2.year)