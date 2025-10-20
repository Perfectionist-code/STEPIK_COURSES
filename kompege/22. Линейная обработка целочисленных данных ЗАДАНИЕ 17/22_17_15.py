def cond(nums: tuple) -> bool:
    return sum((x > mx for x in nums)) >= 1


with open('22_17_15.txt') as file:
    a = [int(x) for x in file]
ans = []
mx = max(filter(lambda x: x % 19 == 0, a))
for x in zip(a, a[1:]):
    if cond(x):
        ans.append(sum(x))
print(len(ans), min(ans))
