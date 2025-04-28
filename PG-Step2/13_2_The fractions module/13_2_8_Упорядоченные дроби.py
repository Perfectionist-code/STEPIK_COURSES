from fractions import Fraction as F
n = int(input())
res = set()
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i / j < 1:
            res.add(F(i)/F(j))
print(*sorted(res), sep = '\n')