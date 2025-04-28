# from random import sample
# from string import ascii_uppercase as asc, digits as dig
# from sympy import flatten
#
# def generate_index():
#     res = [sample(asc, 2), sample(dig, 2), '_', sample(dig, 2), sample(asc, 2)]
#     return ''.join(flatten(res))
#
# print(generate_index())

from random import choice
from string import ascii_uppercase as asc, digits as dig


def generate_index():

    return f'{choice(asc)}{choice(asc)}{choice(dig)}{choice(dig)}_{choice(dig)}{choice(dig)}{choice(asc)}{choice(asc)}'

print(generate_index())