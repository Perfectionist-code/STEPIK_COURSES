from fractions import Fraction


def f(n):
    if n < 2: return 1
    if n >= 2 and n % 3: return f(n - 1) + 17
    return f(Fraction(n, 3)) - 1


res = []
for n in range(100000):
    print(d := f(n))
    if d == 110:
        print('-----' * 5)
        print(n)
        break
