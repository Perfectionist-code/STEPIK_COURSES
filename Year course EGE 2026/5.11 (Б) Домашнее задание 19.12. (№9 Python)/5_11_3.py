with open('03.txt') as file:
    cnt = 0
    for s in file:
        l = sorted(map(int, s.split()))
        l_rep_3 = tuple(x for x in l if l.count(x) == 3)
        l_rep_2 = tuple(x for x in l if l.count(x) == 2)
        l_fr = tuple(x for x in l if l.count(x) == 1)
        if len(set(l_rep_3)) == 1 and len(set(l_rep_2)) == 1 and max(l_rep_2[0], l_rep_3[0]) > max(l_fr):
            print(*l)
            cnt += 1
print('------' * 5)
print(cnt)
