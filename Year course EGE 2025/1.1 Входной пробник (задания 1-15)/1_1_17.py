with open('17.txt') as file:
    a = [int(x) for x in file]
max_el_100 = max(x for x in a if x % 1000 == 100)
res = []
for x, y, z in zip(a, a[1:], a[2:]):
    if ((99 < x < 1000) + (99 < y < 1000) + (99 < z < 1000)) == 2 and (s := sum((x, y, z))) <= max_el_100:
        res.append(s)
        print(x, y, z)
print(len(res), max(res))
