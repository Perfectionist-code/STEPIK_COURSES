def num_to_cs(n: int, cs:int) -> str:
    res = []
    while n:
        n, r = divmod(n, cs)
        res.append(str(r))
    return ''.join(res[::-1])


def get_r(n: int):
    r = num_to_cs(n, 3)
    if not n % 3:
        r = '1' + r + '02'
    else:
        o = num_to_cs((n % 3) * 4,3)
        r += o
    return int(r, 3)


for num in range(1000, 1,-1):
    if (d := get_r(num)) < 199:
        print(num)
        break
