with open('07.txt') as file:
    cnt = 0
    for s in file:
        l = sorted(map(int, s.split()))
        if len(set(l)) == len(l) and 3 * (l[0] + l[-1]) >= 2 * sum(l[1:-1]):
            print(*l)
            cnt += 1
print('------' * 5)
print(cnt)
