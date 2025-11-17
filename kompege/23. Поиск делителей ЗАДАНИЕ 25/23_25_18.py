def is_prime(num: int) -> bool:
    return x > 1 and all(num % d for d in range(2, int(num ** 0.5) + 1))


for x in range(55_000_000, 60_000_001):
    t = x
    while t % 2 == 0:
        t //= 2
    if int(t ** 0.25) ** 4 == t and is_prime(int(t ** 0.25)):
        print(x, t)
