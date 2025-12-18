with open('02.txt') as file:
    cnt = 0
    for s in file:
        l = sorted(map(int, s.split()))
        if l[-1] < sum(l[:-1]) and len(set(l)) == len(l) - 1:
            print(*l)
            cnt += 1
print('----' * 10)
print(cnt)
