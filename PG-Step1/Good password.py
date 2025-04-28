from string import ascii_lowercase, ascii_uppercase, digits


def is_password_good(password):
    return len(password) > 7 and ({*password} & {*ascii_lowercase}) != set() and (
                {*password} & {*ascii_uppercase}) != set() and ({*password} & {*digits}) != set()


# считываем данные
txt = input()
# вызываем функцию
print(is_password_good(txt))
