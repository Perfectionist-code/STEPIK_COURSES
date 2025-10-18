for n in range(50):
    r = f'{n:b}'
    r += r[-1]
    for _ in range(2):
        if r.count('1') % 2:
            r += '1'
        else:
            r += '0'
    if (r:=int(r,2)) > 130:
        print(n)
        break
