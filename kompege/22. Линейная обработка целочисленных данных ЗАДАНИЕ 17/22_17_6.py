with open('22_17_6.txt') as file:
    lst = [int(x) for x in file]
ans = []
for x, y in zip(lst, lst[1:]):
    if abs(x + y) % 3 == 0 and abs(x + y) % 6 != 0 and abs(x * y) % 10 == 8:
        ans.append(x + y)
print(len(ans), max(ans))
