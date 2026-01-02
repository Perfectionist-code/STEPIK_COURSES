with open('17.txt') as file:
    a = [int(x) for x in file]
el_2_d = tuple(x for x in a if 9 < abs(x) < 100)
el = min(el_2_d) + max(el_2_d)
res = []
for tr in zip(a, a[1:], a[2:]):
    if sum(9 < abs(x) < 100 for x in tr) >= 2 and (sm := sum(tr)) > el:
        print(*tr)
        res.append(sm)
print('-----' * 5)
print(len(res), max(res))
