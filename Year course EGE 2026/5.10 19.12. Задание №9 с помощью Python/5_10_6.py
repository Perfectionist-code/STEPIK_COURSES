from statistics import mean

with open('06.txt') as file:
    cnt = 0
    for i, s in enumerate(file, 1):
        l = sorted(map(int, s.split()))
        l_rep = tuple(x for x in l if l.count(x) > 1)
        l_fr = tuple(x for x in l if l.count(x) == 1)
        if len(l_rep) == 4 and len(set(l_rep)) == 2 and mean(l_rep) < max(l_fr):
            print(i)
            break
