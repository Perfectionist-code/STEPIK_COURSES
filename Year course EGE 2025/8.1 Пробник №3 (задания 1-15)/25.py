def get_divisors(num: int):
    divisors = {1,num}
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            divisors.add(d)
            divisors.add(num // d)
            if len(divisors) > 4:
                return []
        return sorted(divisors)


cnt = 0
for n in range(700_001, 10**10):
    divs = get_divisors(n)
    if len(divs) == 4:
        m = max(divs[1:-1]) - min(divs[1:-1])
        if m <= 15:
            print(n, m)
            cnt += 1
        if cnt == 6:
            break
