def num_to_cs(num: int, cs: int):
    res = []
    while num:
        num, r = divmod(num, cs)
        res.append(str(r))
    return ''.join(res[::-1])


def cond_1(nums: tuple) -> bool:
    return any((num_to_cs(x, 3).endswith('2') for x in nums))


with open('22_17_10.txt') as file:
    a = [int(x) for x in file]
ans = []
for x in zip(a, a[1:], a[2:]):
    if cond_1(x):
        ans.append(min(x))
print(len(ans), sum(ans))
