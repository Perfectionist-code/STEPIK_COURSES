# Напишите определение класса Registration
class Registration:
    def __init__(self, login):
        self.login = login

    @staticmethod
    def check_login(login: str) -> bool:
        if not isinstance(login, str):
            raise TypeError
        if login.count('@') != 1 or login.find('@') == 0:
            raise ValueError
        if not ('.' in login[login.index('@'):-1] and login[login.index('@'):-1].index('.') > 1):
            raise ValueError
        return True

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, new_login):
        if Registration.check_login(new_login):
            self.__login = new_login


# Ниже код для проверки класса Registration


try:
    result = Registration("fga")
except ValueError as error:
    print("Логин fga должен содержать один символ '@'")

try:
    result = Registration(1234)
except TypeError as error:
    print("Логин должен быть строкой")

try:
    result = Registration("f@ga@")
except ValueError as error:
    print("Логин f@ga@ должен содержать только один символ '@'")

try:
    result = Registration("fg@a")
except ValueError as error:
    print("В логине fg@a должен быть символ '.' после символа '@'")

try:
    result = Registration("fg.@a")
except ValueError as error:
    print("В логине fg.@a должна быть '.' после символа '@'")

result = Registration("translate@gmail.com")
assert result.login == "translate@gmail.com"
assert result._Registration__login == "translate@gmail.com"

try:
    result.login = "asdsa12asd."
except ValueError as error:
    print("Логин asdsa12asd. должен содержать один символ '@'")

try:
    result.login = "asdsa12@asd"
except ValueError as error:
    print("asdsa12@asd должен быть символ '.' после символа '@'")

result.login = "alligator13@how.do"
assert result.login == "alligator13@how.do"
assert result._Registration__login == "alligator13@how.do"
