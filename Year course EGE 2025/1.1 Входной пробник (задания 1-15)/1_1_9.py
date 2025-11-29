with open('09.txt') as file:
    cnt = 0
    for s in file:
        l = tuple(int(x) for x in s.split())
        l_rep = tuple(x for x in l if l.count(x) > 1)
        l_fr = tuple(x for x in l if l.count(x) == 1)
        if len(l_rep) == 6 and len(set(l_rep)) == 3 and len(l_fr) == 2 and min(l) not in l_rep:
            print(*l)
            cnt += 1
print('----' * 10)
print(cnt)
