with open('05.txt') as file:
    cnt = 0
    for s in file:
        l = sorted(map(int, s.split()))
        l_rep = tuple(x for x in l if l.count(x) > 1)
        l_fr = tuple(x for x in l if l.count(x) == 1)
        if len(l_rep) == 3 and len(set(l_rep)) == 1 and sum(l_rep) ** 2 > sum(l_fr) ** 2:
            print(*l)
            cnt += 1
print('----' * 10)
print(cnt)
