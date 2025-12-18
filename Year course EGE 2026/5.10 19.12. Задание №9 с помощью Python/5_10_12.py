from statistics import mean

with open('12.txt') as file:
    sm = 0
    for s in file:
        l = sorted(map(int, s.split()))
        l_rep_2 = tuple(x for x in l if l.count(x) == 2)
        l_fr = tuple(x for x in l if l.count(x) == 1)
        if ((len(set(l_rep_2)) == 2 and len(l_fr) == 3) + (mean(l[-2:]) <= sum(l[:2]))) == 1:
            sm = sum(l)
            print(*l)
print('----' * 5)
print(sm)
