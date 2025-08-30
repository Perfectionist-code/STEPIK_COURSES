for x in range(1, 101):
    if not ((10 < x ** 3) <= (10 > ((x + 1) * (x + 1) - x))):
        print(x)
