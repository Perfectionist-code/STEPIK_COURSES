def get_R(n: int) -> int:
    r = bin(n)[2:]
    if n % 2:
        r = '1' + r[:-2] + '10'
    else:
        r = '10' + r[2:] + '1'
    return int(r, 2)


res = []
for N in range(34, 1000):
    res.append(get_R(N))
print('Ответ:', min(res))
