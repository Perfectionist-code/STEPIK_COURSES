from string import printable


def f(n: str):
    result = int(f'18{n}89957', 22) + int(f'80{n}33', 22) + int(f'521{n}6', 22)
    return result


for x in printable[:22]:
    if (r := f(x)) % 21 == 0:
        print(r // 21)
        break
