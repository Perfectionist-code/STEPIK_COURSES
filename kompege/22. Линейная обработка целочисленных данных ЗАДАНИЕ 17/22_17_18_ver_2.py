def cond(nums: tuple) -> bool:
    x, y = nums
    return (x % 9 == 0) + (y % 9 == 0) == 1 and (x % 9 == 0 and oct(y)[-1] == '3' or y % 9 == 0 and oct(x)[-1] == '3')


with open('22_17_18.txt') as file:
    a = [int(s) for s in file]
ans = []
for tp in zip(a, a[1:]):
    if cond(tp):
        ans.append(max(tp))
print(len(ans), max(ans))
