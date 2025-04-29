lst = [int(x) for x in input().split()]
d = {lst[-2]: lst[-1]}
for i in range(len(lst) - 3, -1, -1):
    d = {lst[i]: d}
print(d)
