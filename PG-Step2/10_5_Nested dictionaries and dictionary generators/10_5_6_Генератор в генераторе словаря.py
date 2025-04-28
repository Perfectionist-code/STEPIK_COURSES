def is_sorted_divisors(number: int):
    res = []
    for num in range(1, number // 2 + 1):
        if not number % num:
            res.append(num)
    res.append(number)
    return res

numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
# numbers.sort()
result = {key: is_sorted_divisors(key) for key in numbers}
print(result)


# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
# result = {n: [i for i in range(1, n // 2 + 1) if n % i == 0] + [n] for n in numbers}

# from collections import deque
# def get_factors_fast(n):
#     nsqrt = n ** .5
#     factors = deque()
#     if nsqrt.is_integer():
#         factors.append(int(nsqrt))
#     for i in range(int(nsqrt) - nsqrt.is_integer(), 0, -1):
#         if n % i == 0:
#             factors.appendleft(i)
#             factors.append(n // i)
#     return list(factors)
#
# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
# result = {n: get_factors_fast(n) for n in numbers}