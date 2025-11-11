def get_sum_divisors(n: int) -> int:
    divisors = {1, n}
    for d in range(2, int(n ** .5) + 1):
        if not n % d:
            divisors.add(d)
            divisors.add(n // d)
    return sum(divisors)


def f(curr, end):
    if curr > end: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr + get_sum_divisors(curr), end)


print(f(2, 62))
