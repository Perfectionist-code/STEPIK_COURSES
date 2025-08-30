for x in range(1, 30):
    if not (((not (x > 5)) or (x < 20)) <= (x % 5)):
        print(x)
