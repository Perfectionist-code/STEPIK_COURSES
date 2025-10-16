for n in range(50):
    r = f'{n:b}'
    if n % 2:
        r += '10'
    else:
        r += '01'
    if (r:=int(r,2)) > 81:
        print(r)
