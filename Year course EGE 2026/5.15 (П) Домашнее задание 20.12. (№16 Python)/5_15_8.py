def is_prime(num: int) -> bool:
    return num > 1 and all(num % d != 0 for d in range(2, int(num ** .5) + 1))


def f(n):
    if n == 0: return 1
    return 7 * (n - 1) + f(n - 1)


cnt = 0
for n in range(2, 201):
    if is_prime(f(n)):
        cnt += 1
print(cnt)
