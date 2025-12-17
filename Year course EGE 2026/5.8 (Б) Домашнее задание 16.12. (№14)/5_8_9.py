from string import printable


def f(n: str):
    return int(f'abcd{n}', 15) + int(f'123{n}4', 15)


for y in printable[:15]:
    if not (r := f(y)) % 14:
        print(r // 14)
        break
