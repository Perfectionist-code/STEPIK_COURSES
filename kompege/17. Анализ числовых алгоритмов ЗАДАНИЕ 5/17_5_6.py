def get_r(num:int) -> int:
    r = f'{num:b}'
    r = r[::-1].lstrip('0')
    return int(r, 2)

for n in range(1, 101):
    if get_r(n) == 13:
        print(n)