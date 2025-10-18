def is_prime(num: int) -> bool:
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            return False
    return True
i = 0
for n in range(3532000, 3532161):
    if is_prime(n):
        i += 1
        print(i, n)
