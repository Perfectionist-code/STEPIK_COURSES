from statistics import mean

with open('08.txt') as file:
    for i, s in enumerate(file, 1):
        l = tuple(map(int, s.split()))
        l_rep_2 = tuple(x for x in l if l.count(x) == 2)
        l_fr = tuple(x for x in l if l.count(x) == 1)
        if len((set(l_rep_2))) == 2 and len(l_fr) == 3 and mean(l_rep_2) < max(l_fr):
            print(i)
            break
