def to_base4(n: int) -> str:
    if not n:
        return '0'
    res = []
    while n:
        n, r = divmod(n, 4)
        res.append(str(r))
    return ''.join(res[::-1])


r = - 1
num = 1
for num in range(1, 300):
    r = to_base4(num)
    if not num % 4:
        r += r[-2:]
    else:
        r += to_base4((num % 4) * 2)
    r = int(r, 4)
    if r < 369:
        res = num
    print(num, r)
print('ОТВЕТ: ', res)
