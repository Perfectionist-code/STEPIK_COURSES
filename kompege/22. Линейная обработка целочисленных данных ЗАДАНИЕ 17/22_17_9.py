from statistics import mean


def cond_1(nums: tuple) -> bool:
    return any((abs(x) % 12 == 0 for x in nums))


def cond_2(nums: tuple) -> bool:
    return all((abs(x) % 3 == 0 for x in nums))


with open('22_17_9.txt') as file:
    a = [int(x) for x in file]
ans = []
for x in zip(a, a[1:], a[2:]):
    if cond_1(x) and cond_2(x):
        ans.append(mean(x))
print(len(ans), min(ans))
