for n in range(1, 1000):
    N = '1' + bin(n)[2:] + '00'
    if (d:=int(N, 2)) > 400:
        print(n)
        break



