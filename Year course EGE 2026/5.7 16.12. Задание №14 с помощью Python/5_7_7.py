from string import printable


def f(n: str):
    result = int(f'123{n}5', 15) + int(f'1{n}233', 15)
    return result


for x in printable[:15]:
    if (r:=f(x)) % 14 == 0:
        print(r // 14)
        break