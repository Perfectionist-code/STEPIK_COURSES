from math import prod
def f(n):
    if n < 22:
        return 111
    if all((n >= 22, not n % 2)):
        return n + 7 * f(n - 3)
    return 5 * f(n - 1)


res = [int(x) for x in str(f(35) + f(11)) if x != '0']
print(prod(res))
