with open('17_1729262457.txt') as file:
    a = [int(x) for x in file]
res = []
max_el_42_4 = max(x for x in a if 999 < x < 10000 and x % 100 == 42)
print(max_el_42_4)
for t in zip(a, a[1:], a[2:]):
    if sum(abs(x) % 100 == 42 and 999 < abs(x) < 10000 for x in t) >= 2 and (sm := sum(t)) > max_el_42_4:
        print(*t)
        res.append(sm)
print(len(res), max(res))
