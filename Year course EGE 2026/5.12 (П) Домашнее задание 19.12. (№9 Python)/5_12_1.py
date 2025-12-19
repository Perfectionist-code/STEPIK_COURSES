with open('01.txt') as file:
    sm = 0
    for i, s in enumerate(file, 1):
        l = sorted(map(int, s.split()))
        l_rep_3 = tuple(x for x in l if l.count(x) == 3)
        l_fr = sorted(x for x in l if l.count(x) == 1)
        if not l_rep_3 and len(l_fr) >= 2:
            a = l_fr[1]
            l.remove(a)
            if a ** 2 < sum(l):
                print(*l, a)  # Для проверки
                sm += i
print('----' * 10)
print(sm)
