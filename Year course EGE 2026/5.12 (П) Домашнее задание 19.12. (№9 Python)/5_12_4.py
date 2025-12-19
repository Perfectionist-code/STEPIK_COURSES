with open('04.txt') as file:
    cnt = 0
    for i, s in enumerate(file, 1):
        l = sorted(map(int, s.split()))
        l_rep_3 = tuple(x for x in l if l.count(x) == 3)
        l_rep_2 = tuple(x for x in l if l.count(x) == 2)
        l_fr = tuple(x for x in l if l.count(x) == 1)
        if len(set(l_rep_3)) == 1 and len(set(l_rep_2)) == 1 and len(l_fr) == 3 and l_rep_3[0] > l_rep_2[0]:
            cnt += 1
            print(f'{i})', *l)  # Для проверки
            if cnt == 3:
                break
print('----' * 10)
print(i)
