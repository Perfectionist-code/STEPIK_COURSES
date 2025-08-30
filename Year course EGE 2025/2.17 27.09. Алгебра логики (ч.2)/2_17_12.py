A = {14, 31, 40, 1, 12, 94}
B = {40, 12, 10, 1, 13}
cnt = 0
for x in range(1, 100):
    if not ((x in A) <= (x not in B)):
        cnt += 1
        print(x)
print()
print(cnt)
