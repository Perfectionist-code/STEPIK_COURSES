from statistics import mean

with open('07.txt') as file:
    s = 0
    for s in file:
        l = sorted(map(int, s.split()))
        l_rep = tuple(x for x in l if l.count(x) > 1)
        l_fr = tuple(x for x in l if l.count(x) == 1)
        if len(l_rep) == 4 and len(set(l_rep)) == 2 and max(l) not in l_rep:
            print(sum(l))
            break
