from fractions import Fraction as F
from math import gcd

_sum = F(0)
n = int(input())
_numerator = n // 2
_denominator = n - _numerator
while gcd(_numerator, _denominator) != 1:
    _numerator -= 1
    _denominator += 1
print(F(_numerator, _denominator))
