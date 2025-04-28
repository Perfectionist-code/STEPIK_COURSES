# объявление функции
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_even(num):
    return num % 2 == 0


def is_palindrome(text):
    return text == text[::-1]


def is_valid_password(password):
    password = password.split(':')
    if len(password) != 3:
        return False
    for part in password:
        if not part.isdigit():
            return False
    return all([is_palindrome(password[0]), is_prime(int(password[1])), is_even(int(password[2]))])
    # if part.


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
