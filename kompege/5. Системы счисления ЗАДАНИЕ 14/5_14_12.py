for n in range(4, 1000):
    if int('132', n) + int('13', 8) == int('124', n + 1):
        print(n)
        break
