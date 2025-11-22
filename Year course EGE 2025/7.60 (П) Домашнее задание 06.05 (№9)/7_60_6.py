from statistics import mean

with open('06_9-249.txt') as file:
    cnt = 0
    for s in file:
        lst = list(map(int, s.split()))
        l_rep = tuple(x for x in lst if lst.count(x) > 1)
        l_fr = tuple(x for x in lst if lst.count(x) == 1)
        l_rep_3 = tuple(x for x in lst if lst.count(x) >= 3)
        if l_rep_3 and l_fr and mean(l_rep) < mean(l_fr):
            cnt += 1
            print(*lst)
print('------' * 5)
print(cnt)
