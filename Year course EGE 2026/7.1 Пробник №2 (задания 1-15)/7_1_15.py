def get_divisors(num: int):
    return tuple(d for d in range(2, num // 2 + 1) if not num % d)


def f(x):
    A = 3 <= x <= 60
    B = x in B_divisors
    C = x in dy
    return C <= (A and (not B))


B_divisors = get_divisors(177)
for y in range(10000, 1, -1):
    dy = get_divisors(y)
    if dy and all(f(x) for x in range(1, 100000)):
        print(y)
        break
