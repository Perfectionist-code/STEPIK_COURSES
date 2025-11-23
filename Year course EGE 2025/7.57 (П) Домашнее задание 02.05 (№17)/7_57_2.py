from math import prod

with open('02_17_2_1705000691.txt') as file:
    a = [int(x) for x in file]
couples = []
for i in range(2, len(a) - 3):
    couples.append((a[i - 2:i], (a[i:i + 2]), a[i + 2:i + 4]))
print(*couples,sep='\n')
res = []
for c in couples:
    if (s1 := sum(c[1])) > (s0 := sum(c[0])) and s1 > (s2 := sum(c[2])) and all(x > 0 for x in (s0, s1, s2)):
        res.append(prod(c[1]))
print(len(res), min(res))


