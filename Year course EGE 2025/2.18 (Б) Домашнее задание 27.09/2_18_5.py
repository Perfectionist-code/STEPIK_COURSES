for x in range(1, 101):
    if not ((not (x < 4) <= (x>8)) <= (not x % 2)):
        print(x)