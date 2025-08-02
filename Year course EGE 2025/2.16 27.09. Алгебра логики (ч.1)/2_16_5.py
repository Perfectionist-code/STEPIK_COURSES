tup = (30, 42, 21, 45)
for i, num in enumerate(tup, 1):
    if ((not num % 2) or (not num % 3)) and (not num % 7):
        print(i, num)
