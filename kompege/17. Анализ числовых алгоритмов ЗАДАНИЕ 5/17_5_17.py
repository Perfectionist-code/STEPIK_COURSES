from itertools import permutations


def get_r(n: int):
    l = [x for x in str(n)]
    nums = [int(''.join(per)) for per in permutations(l, 2)]
    nums = [x for x in nums if 9 < x < 100]
    return max(nums) - min(nums)


for num in range(100, 1000):
    if get_r(num) == 5:
        print(num)
        break


