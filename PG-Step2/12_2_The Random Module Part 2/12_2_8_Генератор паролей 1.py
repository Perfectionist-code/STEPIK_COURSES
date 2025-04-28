from string import ascii_letters, digits
from random import choices, shuffle


def generate_password(*args):
    correct_chr = ''.join(set(ascii_letters + digits) - set('0oOIl1'))
    print(correct_chr)
    # res =
    return ''.join(choices(correct_chr, k = length_password))


def generate_passwords(*args):
    return [generate_password(length_password) for _ in range(number_passwords)]


number_passwords = int(input())
length_password = int(input())
print(*generate_passwords(number_passwords, length_password), sep = '\n')
