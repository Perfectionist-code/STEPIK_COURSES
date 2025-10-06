def get_R(n: int) -> int:
    r = bin(n)[2:]
    if n % 2:
        r = '1' + r + '01'
    else:
        r = '10' + r
    return int(r, 2)


res = []
for N in range(1, 13):
    res.append(get_R(N))
print('Ответ:', max(res))
