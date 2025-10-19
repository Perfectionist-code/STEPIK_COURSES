def cond_1(nums: tuple) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            continue
        else:
            return False
    return True


def cond_2(nums: tuple) -> bool:
    return max(nums) - min(nums) > 1000


with open('22_17_11.txt') as file:
    a = [int(x) for x in file]
ans = []
for x in zip(a, a[1:], a[2:], a[3:]):
    if cond_1(x) and cond_2(x):
        ans.append(sum(x))
print(len(ans), min(ans))
