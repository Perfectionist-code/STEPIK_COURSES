# Напишите определение класса Registration
from string import digits, ascii_uppercase, ascii_lowercase, ascii_letters


class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @staticmethod
    def check_login(login: str) -> bool:
        if not isinstance(login, str):
            raise TypeError
        if login.count('@') != 1 or login.find('@') == 0:
            raise ValueError
        if not ('.' in login[login.index('@'):-1] and login[login.index('@'):-1].index('.') > 1):
            raise ValueError
        return True

    @staticmethod
    def is_include_digit(password: str) -> bool:
        # for digit in digits:
        #     if digit in password:
        #         return True
        # return False
        return bool(set(digits) & set(password))

    @staticmethod
    def is_include_all_register(password: str) -> bool:
        password_set = set(password)
        return bool(password_set & set(ascii_lowercase)) and bool(password_set & set(ascii_uppercase))

    @staticmethod
    def is_include_only_latin(password: str) -> bool:
        return bool(set(password) - set(ascii_letters + digits))

    @staticmethod
    def check_password_dictionary(password: str) -> bool:
        with open('easy_passwords.txt', 'r') as file:
            for item in file:
                if password == item.strip():
                    file.close()
                    return True
        file.close()
        return False

    @staticmethod
    def check_password(password: str) -> bool:
        if not isinstance(password, str):
            raise TypeError("Пароль должен быть строкой")
        if not 4 < len(password) < 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_digit(password):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(password):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if Registration.is_include_only_latin(password):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if Registration.check_password_dictionary(password):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        return True

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, new_login):
        if Registration.check_login(new_login):
            self.__login = new_login

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        if Registration.check_password(new_password):
            self.__password = new_password

# Ниже код для проверки класса Registration


try:
    s2 = Registration("fga", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError("Registration('fga', 'asd12') как можно записать такой логин?")

try:
    s2 = Registration("fg@a", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError("Registration('fg@a', 'asd12') как можно записать такой логин?")

s2 = Registration("translate@gmail.com", "as1SNdf")
try:
    s2.login = "asdsa12asd."
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12asd как можно записать такой логин?")

try:
    s2.login = "asdsa12@asd"
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12@asd как можно записать такой логин?")

assert Registration.check_password_dictionary('QwerTy123'), 'проверка на пароль в слове не работает'

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError("QwerTy123 хранится в словаре паролей, как его можно было сохранить?")


try:
    s2.password = "KissasSAd1f"
except ValueError as e:
    pass
else:
    raise ValueError("KissasSAd1f хранится в словаре паролей, как его можно было сохранить?")

try:
    s2.password = "124244242"
except ValueError as e:
    pass
else:
    raise ValueError("124244242 пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "RYIWUhjkdbfjfgdsffds"
except ValueError as e:
    pass
else:
    raise ValueError("RYIWUhjkdbfjfgdsffds пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "CaT"
except ValueError as e:
    pass
else:
    raise ValueError("CaT пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "monkey"
except ValueError as e:
    pass
else:
    raise ValueError("monkey пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError("QwerTy123 пароль есть в слове, нельзя его использовать")

try:
    s2.password = "HelloQEWq"
except ValueError as e:
    pass
else:
    raise ValueError("HelloQEWq пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = [4, 32]
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

try:
    s2.password = 123456
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

print('U r hacked Pentagon')
