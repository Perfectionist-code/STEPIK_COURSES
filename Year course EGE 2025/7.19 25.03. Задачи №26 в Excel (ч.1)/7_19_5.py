with open('05.txt') as file:
    n = int(file.readline())
    print(n)
    a = sorted(int(x) for x in file)
res = []
while len(a) > 2:
    x, y = a[:2]
    z = a[-1]
    res.append((x, y, z))
    for l in (x, y, z):
        a.remove(l)
res.append(a)
s = 0
for tp in res:
    s += sum(tp[:2])
print(s)

