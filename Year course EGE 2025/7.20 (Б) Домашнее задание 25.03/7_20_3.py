with open('03.txt') as file:
    lst = [int(x) for x in file]
lst7 = [x for x in lst if x % 10 == 7]
cnt7 = len(lst7)
res = []
for a, b in zip(lst, lst[1:]):
    if ((a < 0 and b > 0) or (a > 0 and b < 0)) and (s := a + b) < cnt7:
        res.append(s)
print(len(res), max(res))
