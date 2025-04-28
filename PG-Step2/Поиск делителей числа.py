from collections import deque

def get_factors_fast(n):
    nsqrt = n ** .5
    factors = deque()
    if nsqrt.is_integer():
        factors.append(int(nsqrt))
    for i in range(int(nsqrt) - nsqrt.is_integer(), 0, -1):
        if n % i == 0:
            factors.appendleft(i)
            factors.append(n // i)
    return list(factors)

print(len(get_factors_fast(int(input()))))

# def count_divisors(n):
#     rootn = n ** .5
#     count = 0
#     return sum(2 for i in range(1, int(rootn) + 1) if not n % i) - (rootn % 1 == 0)
#
# print(count_divisors(int(input())))


# from sympy import divisors
#
# print(len(divisors(int(input()))))


# print(__import__('sympy').divisor_count(int(input())))

def count_divisors(n):
    c = 1
    for i in range(2, int(n ** .5)):
        p = 1
        while not n % i:
            p += 1
            n //= i
        c *= p

    if n > 1:
        c *= 2

    return c


n = int(input())
print(count_divisors(n))