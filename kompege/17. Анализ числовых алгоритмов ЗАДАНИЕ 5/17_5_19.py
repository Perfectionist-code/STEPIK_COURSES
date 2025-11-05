def get_r(n: int):
    n = str(n)
    nums = [int(n[i:i + 2]) for i in range(len(n) - 1)]
    return max(nums) - min(nums)


for num in range(10, 1000):
    if get_r(num) == 44:
        print(num)
        break
