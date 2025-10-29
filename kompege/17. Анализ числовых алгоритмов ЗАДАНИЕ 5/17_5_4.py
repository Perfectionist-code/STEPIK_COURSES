def get_r(num: int) -> int:
    r = f'{num:b}'
    r += r[-1]
    for _ in range(2):
        if r.count('1') % 2 == 0:
            r += '0'
        else:
            r += '1'
    return int(r, 2)

for n in range(1, 101):
    if (R:=get_r(n)) > 144:
        print(R)
