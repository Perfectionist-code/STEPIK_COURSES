from fractions import Fraction as F

m, n = input(), input()
print(f'{m} + {n} = {F(m) + F(n)}')
print(f'{m} - {n} = {F(m) - F(n)}')
print(f'{m} * {n} = {F(m) * F(n)}')
print(f'{m} / {n} = {F(m) / F(n)}')
