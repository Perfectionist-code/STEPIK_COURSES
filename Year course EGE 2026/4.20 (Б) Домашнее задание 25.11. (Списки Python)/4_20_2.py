lst = [int(input()) for _ in range(int(input()))]
res = []
for num in lst:
    if num in res:
        continue
    if num > 0:
        res.append(num)
print(*res, sep='\n')
