with open('17_20558.txt') as file:
    a = [int(x) for x in file]
min_pos_123 = min([x for x in a if x > 0 and x % 1000 == 123])
print(min_pos_123)
res = []
for x, y in sorted(zip(a, a[1:])):
    if (r := abs(x-y)) <= min_pos_123:
        res.append(r)
print(len(res), max(res))
