with open('04.txt') as file:
    cnt = 0
    for s in file:
        l = list(map(int, s.split()))
        l_rep_3 = tuple(x for x in l if l.count(x) == 3)
        l_fr = tuple(x for x in l if l.count(x) == 1)
        if len(set(l_rep_3)) == 1 and len(l_fr) == 3 and sum(l_rep_3) ** 2 > sum(l_fr) ** 2:
            print(*l)
            cnt += 1
print('------' * 5)
print(cnt)
