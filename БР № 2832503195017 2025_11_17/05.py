def get_r(num: int):
    r = f'{num:b}'
    for _ in range(2):
        r += str(sum((int(x) for x in r)) % 2)
    return int(r, 2)

for n in range(1,100):
    if (R:=get_r(n)) >80:
        print(R)
        break