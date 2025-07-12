for n in range(1, 1000):
    R1 = bin(n)[2:]
    if (s1:=R1.count('1')) > (s0:=R1.count('0')):
        R = R1 + '00'
    elif s1 < s0:
        R = R1 + '11'
    else:
        R = R1 + '10'
    if int(R, 2) <= 1000:
        print(n)

