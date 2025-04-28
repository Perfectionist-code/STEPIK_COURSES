cnt = 0
lst = list(map(int, input().split()))
for i in range(1, len(lst)):
    if lst[i - 1] < lst[i]:
        cnt += 1
print(cnt)
