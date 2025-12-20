with open('01.txt') as file:
    cnt = 0
    for s in file:
        l = sorted(map(int, s.split()))
        if l[0] + l[-1] <= sum(l[1:-1]):
            print(*l)
            cnt += 1
print('------' * 5)
print(cnt)
