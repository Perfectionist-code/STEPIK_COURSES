from math import prod


def cond_1(nums: tuple) -> bool:
    return sum(nums) >= 100


def cond_2(nums: tuple) -> bool:
    return any((x < 0 for x in nums))


with open('22_17_12.txt') as file:
    a = [int(x) for x in file]
ans = []
for x in zip(a, a[1:]):
    if cond_1(x) and cond_2(x):
        ans.append(prod(x))
print(len(ans), max(ans))
