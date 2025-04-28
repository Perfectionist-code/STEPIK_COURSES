from fractions import Fraction as F
from math import factorial as fact
_sum = F(0)
n = int(input())
for i in range(1,n + 1):
    _sum += F(1) / F(fact(i))
print(_sum)


