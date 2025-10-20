from statistics import mean


def cond(nums: tuple) -> bool:
    return sum((x > mean_file for x in nums)) >= 2


with open('22_17_14.txt') as file:
    a = [int(x) for x in file]
ans = []
mean_file = mean(a)
for x in zip(a, a[1:], a[2:]):
    if cond(x):
        ans.append(sum(x))
print(len(ans), max(ans))
