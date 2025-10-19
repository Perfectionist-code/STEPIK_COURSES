def is_prime(num: int) -> bool:
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            return False
    return True


cnt = 0
for n in range(7178551, 7178660):
    if is_prime(n):
        cnt += 1
        print(cnt, n)
