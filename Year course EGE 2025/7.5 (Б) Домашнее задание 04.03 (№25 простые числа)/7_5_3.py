def is_prime(num: int) -> bool:
    for d in range(2, int(num ** .5) + 1):
        if not num % d:
            return False
    return True


ans = 0
for n in range(2,20001):
    if is_prime(n):
        ans += 1
print('---' * 10)
print(ans)
