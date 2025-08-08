tup = (33, 20, 15, 21)
for i, num in enumerate(tup, 1):
    if ((not num % 2) == (num > 8)) <= (num < 20):
        print(i, num, sep='. ')
