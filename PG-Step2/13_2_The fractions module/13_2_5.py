from fractions import Fraction as F
_sum = F(0)
n = int(input())
for i in range(1,n + 1):
    _sum += F(1) / F(i) ** 2
print(_sum)


