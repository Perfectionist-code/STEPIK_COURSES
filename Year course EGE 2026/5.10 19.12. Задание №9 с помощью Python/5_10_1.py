with open('01.txt') as file:
    cnt = 0
    for s in file:
        l = sorted(map(int, s.split()))
        if l[-1] < sum(l[:-1]) and l[0] + l[-1] == l[1] + l[2]:
            print(*l)
            cnt += 1
print('----' * 10)
print(cnt)
