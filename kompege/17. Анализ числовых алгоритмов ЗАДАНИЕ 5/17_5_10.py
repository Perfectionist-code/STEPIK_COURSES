def get_r(n: int):
    r = f'{n:b}'
    if not (sum(int(x) for x in r) % 2):
        r = '10' + r[2:] + '0'
    else:
        r = '11' + r[2:] + '1'
    return int(r, 2)


for num in range(1, 1000):
    if (d:=get_r(num)) < 35:
        print(num)


