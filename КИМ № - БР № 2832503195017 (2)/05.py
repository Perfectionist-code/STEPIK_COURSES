def num_to_cs(num: int, cs):
    res = []
    while num:
        num, r = divmod(num, cs)
        res.append(str(r))
    return ''.join(res[::-1])


def f(n):
    r = num_to_cs(n, 3)
    if n % 2 == 0:
        r = '1' + r + '00'
    else:
        s = num_to_cs(sum((int(x) for x in r)), 3)
        r += s
    return r

for N in range(1, 1000):
    R = int(f(N), 3)
    if R > 168:
        print(N)
        break
