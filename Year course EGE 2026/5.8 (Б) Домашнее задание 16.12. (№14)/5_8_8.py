from string import printable


def f(n: str):
    return int(f'7{n}38596', 23) + int(f'14{n}36', 23) + int(f'61{n}7', 23)


for x in printable[:23]:
    if not (r := f(x)) % 22:
        print(r // 22)
        break
