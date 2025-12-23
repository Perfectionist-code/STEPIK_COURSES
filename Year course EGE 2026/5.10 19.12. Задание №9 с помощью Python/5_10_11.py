with open('11.txt') as file:
    sm = 0
    for s in file:
        l = sorted(map(int, s.split()))
        l_rep_3 = tuple(x for x in l if l.count(x) == 3)
        l_rep_2 = tuple(x for x in l if l.count(x) == 2)
        l_fr = tuple(x for x in l if l.count(x) == 1)
        if len(l_rep_3) == 3 and len(l_rep_2) == 2 and len(l_fr) == 2 and l_rep_3[0] > l_rep_2[0]:
            sm += l[0]
            print(*l)
print('----' * 5)
print(sm)
