with open('22_17_7.txt') as file:
    lst = [int(x) for x in file]
ans = []
for x, y in zip(lst, lst[1:]):
    if x * y > 0 and abs(x + y) % 7 == 0:
        ans.append(x * y)
print(len(ans), min(ans))
