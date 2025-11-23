def get_r(num: int):
    a = (sum(int(x) for x in str(num) if int(x) % 2 == 0)) ** 2
    # print(a)
    l = tuple(map(int, str(num)))
    b = (max(l) - min(l)) ** 3
    # print(b)
    res = sorted((a, b))
    res = tuple(str(x) for x in res)
    r = ''.join(res)
    # print(r)
    return int(r)

for n in range(1000,10000):
    if get_r(n) == 4343:
        print(n)
        break