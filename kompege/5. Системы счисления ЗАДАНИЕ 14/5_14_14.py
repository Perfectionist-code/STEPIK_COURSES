for n in range(1, 1000):
    try:
        if int('21', n) * int('13', n) == int('313', n):
            print(n)
            break
    except:
        continue