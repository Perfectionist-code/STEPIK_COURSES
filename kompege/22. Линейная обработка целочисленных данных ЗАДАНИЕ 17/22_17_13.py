def cond_1(nums: tuple) -> bool:
    return 50 <= sum((abs(x) for x in nums)) <= 200


with open('22_17_13.txt') as file:
    a = [int(x) for x in file]
ans = []
for x in zip(a, a[1:]):
    if cond_1(x):
        ans.append(min(x))
print(len(ans), min(ans))