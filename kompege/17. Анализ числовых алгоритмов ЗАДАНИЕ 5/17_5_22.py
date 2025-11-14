from math import prod


def f(n: int, m: int):
    even_n = [int(x) for x in str(n) if not int(x) % 2 and int(x) != 0]
    even_m = [int(x) for x in str(m) if not int(x) % 2 and int(x) != 0]
    odd_m = [int(x) for x in str(m) if int(x) % 2]
    odd_n = [int(x) for x in str(n) if int(x) % 2]
    P1 = prod(even_n) * prod(even_m)
    P2 = prod(odd_n) * prod(odd_m)
    return abs(P1 - P2)


for M in range(1, 1000):
    if f(120, M) == 29:
        print(M)
        break
