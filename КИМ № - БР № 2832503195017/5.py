def f(n: int):
    r = f'{n:b}'
    if not n % 3:
        r += r[-3:]
    else:
        r += f'{(n % 3)*3:b}'
    return int(r, 2)

res = []
for num in range(1,10000):
    if (R:=f(num)) > 151:
        res.append(R)
print(min(res))


