def get_r(num: int):
    r = f'{num:b}'
    if not num % 2:
        r = r.replace('1', '11')
    else:
        r = r.replace('0', '00')
    return int(r, 2)


for n in range(1, 100):
    if get_r(n) > 70:
        print(n)
        break
