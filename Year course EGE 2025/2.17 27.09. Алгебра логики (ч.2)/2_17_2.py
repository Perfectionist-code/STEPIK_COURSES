for x in range(1, 40):
    if not (((x > 2) and (x < 30)) or ((x % 2) <= (x > 5))):
        print(x)
