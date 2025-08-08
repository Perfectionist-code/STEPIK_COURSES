for x in range(1, 101):
    if not (((not x % 3) and (not x % 5)) <= (not (x > 40))):
        print(x)