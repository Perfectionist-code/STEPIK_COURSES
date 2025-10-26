def is_prime(num: int) -> bool:
    if num == 1: return False
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            return False
    return True


def get_divisors(num: int):
    divisors = set()
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
    return divisors

cnt = 0

for n in range(1_325_000, 0, -1):
    pr_divs = [x for x in get_divisors(n) if is_prime(x)]
    s = sum(pr_divs)
    if 0 < s < 30000 and s % 5 == 0:
        print(n)
        cnt +=1
    if cnt == 5:
        break

# Ответ:
# 1325000
# 1324994
# 1324992
# 1324991
# 1324986
# 3 часа 50 минут