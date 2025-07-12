res = 0
trigger = set('dw')
for _ in range(int(input())):
    if (set(input()) & trigger).__len__() == 2:
        res += 1
print(res)
