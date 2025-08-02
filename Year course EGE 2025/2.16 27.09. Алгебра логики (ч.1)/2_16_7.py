tup = (30, 79, 21, 45)
for i, num in enumerate(tup, 1):
    if (num % 2) or (not num % 5) and (not num % 3):
        print(i, num)