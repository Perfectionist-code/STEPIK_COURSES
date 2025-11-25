with open('17var01.txt') as file:
    a = [int(x) for x in file]
min_element = min(a)
res = []
for x, y in zip(a, a[1:]):
    if x % 27 == min_element or y % 27 == min_element:
        res.append(x + y)
print(len(res), max(res))
