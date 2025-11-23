with open('01.txt') as file:
    a = [int(x) for x in file]
max_el = max(x for x in a if 999 < x < 10000 and x % 100 == 22)
res = []
for t in zip(a, a[1:], a[2:]):
    if len(set([len(str(abs(x))) for x in t])) == 3 and (sm := sum(t)) >= max_el:
        res.append(sm)
        print(*t, '|', sm)
print(len(res), max(res))

