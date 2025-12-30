from statistics import mean

with open('06.txt') as file:
    cnt = 0
    for s in file:
        l = list(map(int, s.split()))
        l_rep_2 = tuple(x for x in l if l.count(x) == 2)
        l_fr = tuple(x for x in l if l.count(x) == 1)
        if len(set(l_rep_2)) == 3 and len(l_fr) == 1 and mean((max(l_rep_2), min(l_rep_2))) < l_fr[0]:
            print(*l)
            cnt += 1
print('------' * 5)
print(cnt)
