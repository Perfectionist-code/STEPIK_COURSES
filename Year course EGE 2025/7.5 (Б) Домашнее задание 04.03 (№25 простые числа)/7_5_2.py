def is_prime(num: int) -> bool:
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            return False
    return True


ans = 0
for n in range(1060, 18814):
    if is_prime(n):
        ans += n
        print(n)
print('---' * 10)
print(ans)
