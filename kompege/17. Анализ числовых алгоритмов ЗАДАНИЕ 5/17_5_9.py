def get_r(n: int):
    r = f'{n:b}'
    if not n % 2:
        r = '1' + r + '0'
    else:
        r = '11' + r + '11'
    return int(r, 2)


for num in range(1, 100):
    if (d:=get_r(num)) > 52:
        print(d)


