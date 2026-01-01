def get_r(num: int) -> int:
    r = f'{num:b}'
    if num % 3:
        r += f'{(num % 3 + 1) * 3:b}'
    else:
        r += r[-3:]
    return int(r, 2)


res = []
for n in range(1, 1000):
    if (R := get_r(n)) <= 416:
        res.append(R)
print(max(res))
