def num_to_cs(n: int, cs:int) -> str:
    res = []
    while n:
        n, r = divmod(n, cs)
        res.append(str(r))
    return ''.join(res[::-1])


def get_r(n: int):
    r = num_to_cs(n, 6)
    if not (ost:=n % 3):
        r += r[2:]
    else:
        r += num_to_cs(ost * 10,6)
    return int(r, 6)


for num in range(1, 100):
    if (d := get_r(num)) > 680:
        print(d)

