from statistics import mean

with open('03.txt') as file:
    cnt = 0
    for s in file:
        l = sorted(map(int, s.split()))
        l_rep = tuple(x for x in l if l.count(x) > 1)
        l_fr = tuple(x for x in l if l.count(x) == 1)
        if len(l_rep) == 2 and mean(l_fr) <= sum(l_rep):
            print(*l)
            cnt += 1
print('----' * 10)
print(cnt)
