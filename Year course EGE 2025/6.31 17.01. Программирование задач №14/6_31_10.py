from string import printable


def f(n: str):
    return int(f'3364{n}', 11) + int(f'{n}7946', 12) == int(f'55{n}87', 14)



for x in printable[:11]:
    if f(x):
        print(int(f'55{x}87', 14))
        break
