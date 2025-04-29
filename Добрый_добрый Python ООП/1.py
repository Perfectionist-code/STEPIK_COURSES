n = int(input())
lst_m = sorted([int(x) for x in input().split()])
m = int(input())
lst_w = sorted([int(x) for x in input().split()])
cnt = 0
for i, val_m in enumerate(lst_m):
    for j, val_w in enumerate(lst_w):
        try:
            a = abs(val_m-val_w)
            if a < 2:
                cnt += 1
                lst_m[i] = None
                lst_w[j] = None
                break
        except TypeError:
            continue
print(cnt)
#Данный файл был изменён
print('Go')