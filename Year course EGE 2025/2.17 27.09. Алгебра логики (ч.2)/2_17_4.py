for x in range(1, 100):
    if not (((not x % 3) == (x < 8)) or ((x < 30) <= (not x % 5))):
        print(x)