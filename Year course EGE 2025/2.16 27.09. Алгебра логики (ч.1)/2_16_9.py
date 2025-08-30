tup = (35, 45, 84, 15)
for i, num in enumerate(tup, 1):
    n = not bool(int(str(num)[0]) % 2)
    if (n and (not num % 5)) or (not num % 3):
        print(i, num)