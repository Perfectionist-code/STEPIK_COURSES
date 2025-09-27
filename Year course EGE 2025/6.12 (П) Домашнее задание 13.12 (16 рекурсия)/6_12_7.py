from sympy import isprime


def f(n):
    if n == 0: return 1
    return 7 * (n - 1) + f(n - 1)


cnt = 0
for i in range(2, 201):
    if isprime(f(i)):
        cnt += 1
print(cnt)
