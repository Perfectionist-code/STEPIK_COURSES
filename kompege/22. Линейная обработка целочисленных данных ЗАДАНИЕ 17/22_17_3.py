lst = [int(x) for x in open('22_17_3.txt')]
res = tuple(filter(lambda x: (x % 10 == 5 or x % 10 == 7) and (bool(x % 9) and bool(x % 11)), lst))
print(len(res), max(res) + min(res))
