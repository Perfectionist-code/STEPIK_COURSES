from math import prod

with open('22_17_8.txt') as file:
    lst = [int(x) for x in file]
ans = []
for x in zip(lst, lst[1:], lst[2:]):
    if abs(prod(x)) % 7 == 0 and abs(sum(x)) % 10 == 5:
        ans.append(sum(x))
print(len(ans), max(ans))
