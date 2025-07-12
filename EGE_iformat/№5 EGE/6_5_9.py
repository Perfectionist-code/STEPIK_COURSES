for n in range(11, 1000):
    R = bin(n)[2:]
    R = '11' + R[:-2] + '11'
    R = R[0] + '00' + R[3:]
    if int(R,2) > 42:
        print(n)
        break
