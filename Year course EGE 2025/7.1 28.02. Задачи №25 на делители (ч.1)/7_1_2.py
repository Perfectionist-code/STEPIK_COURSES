def find_divisors(num: int):
    cnt = 0
    res = [1, num]
    for d in range(2, num // 2 + 1):
        if not (num % d):
            cnt += 1
            res.append(d)
    res.sort()
    return (False, tuple(res)[2:])[len(res) == 4]


result = []
for i in range(154026, 154044):
    if divisors := find_divisors(i):
        result.append(divisors)
result =sorted(result, key=lambda x: x[::-1])
for tup in result:
    print(*tup)
