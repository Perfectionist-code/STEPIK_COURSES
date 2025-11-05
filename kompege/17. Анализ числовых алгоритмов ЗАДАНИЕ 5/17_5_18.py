from itertools import permutations


def get_r(n: int):
    l = [x for x in str(n)]
    nums = [int(''.join(per)) for per in permutations(l, 2)]
    nums = [x for x in nums if 9 < x < 100]
    return max(nums) - min(nums)


cnt = 0
for num in range(300, 400):
    if get_r(num) == 20:
        cnt += 1
print(cnt)
