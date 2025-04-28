from random import choices, choice, shuffle


def generate_password(*args):
    correct_chr = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
    res = list(choice(correct_chr[:24]) + choice(correct_chr[24:48]) + choice(correct_chr[48:]))
    res.extend(choices(correct_chr, k = length_password - 3))
    shuffle(res)
    return ''.join(res)


def generate_passwords(*args):
    return [generate_password(length_password) for _ in range(number_passwords)]


number_passwords = int(input())
length_password = int(input())
print(*generate_passwords(number_passwords, length_password), sep = '\n')
