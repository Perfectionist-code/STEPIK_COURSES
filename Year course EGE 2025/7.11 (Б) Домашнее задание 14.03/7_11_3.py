def get_R(n: int) -> int:
    r = bin(n)[2:]
    if n % 2:
        r = '11' + r + '11'
    else:
        r = '1' + r + '0'
    return int(r, 2)


res = []
for N in range(1, 1000):
    if (R := get_R(N)) > 48:
        res.append(R)
print('Ответ:', min(res))
