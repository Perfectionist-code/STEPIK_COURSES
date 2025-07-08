lst = [int(input()) for _ in range(3)]
res = set(lst).__len__()
if res == 3:
    res = 0
elif res == 2:
    res = 2
else:
    res = 3
print(res)