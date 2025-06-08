class Date():
    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    def isoformat(self):
        return f"{self._year:04}-{self._month:02}-{self._day:02}"

    def format(self):
        return f"{self._day:02}/{self._month:02}/{self._year:04}"


class DateEurope(Date):
    pass


class DateUSA(Date):

    def format(self):
        return f"{self._month:02}/{self._day:02}/{self._year:04}"


# print(issubclass(DateUSA, Date))
# print(issubclass(DateEurope, Date))
#
# d = DateEurope(5, 12, 2001)
# print(d.format())
# print(d.isoformat())
# print(isinstance(d, DateEurope))
# print(isinstance(d, Date))
#
# d = DateUSA(1, 5, 890)
# print(d.format())
# print(d.isoformat())
# print(isinstance(d, DateEurope))
# print(isinstance(d, Date))
# print(isinstance(d, DateUSA))