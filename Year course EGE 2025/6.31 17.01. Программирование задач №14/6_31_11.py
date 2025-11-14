from string import printable


def f(x: str, y: str):
    return int(f'123{x}5', 15) + int(f'67{y}9', 17)


for x in printable[:15]:
    for y in printable[:17]:
        if (r := f(x, y)) % 131 == 0:
            print(y, r // 131)
