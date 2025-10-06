def num_to_cs(num: int, cs: int):
    result = []
    while num:
        num, r = divmod(num, cs)
        result.append(str(r))
    return ''.join(result[::-1])


def get_R(n: int) -> int:
    r = num_to_cs(n, 3)
    if n % 3:
        r = r + num_to_cs(n % 3 * 5, 3)
    else:
        r = r + r[-2:]
    return int(r, 3)


res = []
for N in range(1, 1000):
    if (R := get_R(N)) > 133:
        res.append(R)
print('Ответ:', min(res))
