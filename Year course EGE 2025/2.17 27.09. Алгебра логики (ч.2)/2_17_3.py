for x in range(1, 1000):
    if not (((not x % 3) and (not x % 5)) <= (not (x > 15))):
        print(x)
