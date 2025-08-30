A = {24, 33, 41, 15, 18}
B = {3, 35, 41, 18, 9}
cnt = 0
for x in range(1, 100):
    if not ((x not in A) and (x not in B)):
        cnt += 1
        print(x)
print()
print(cnt)

