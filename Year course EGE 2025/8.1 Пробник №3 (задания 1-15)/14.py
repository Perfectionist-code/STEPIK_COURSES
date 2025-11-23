from string import printable

pr = printable[:36].upper()
print(pr)


def num_to_10(x: int, y: int):
    n1 = pr.index('W') + x * 190 + pr.index('N') * 190 ** 2
    n2 = pr.index('R') + pr.index('A') * 190 + y * 190 ** 2 + pr.index('Y') * 190 ** 3
    return n1 + n2


res = []
for x in range(0, 190):
    for y in range(0, 190):
        if (num := num_to_10(x, y)) % 189==0:
            res.append((x*y, num // 189))
print(max(res)[1])
