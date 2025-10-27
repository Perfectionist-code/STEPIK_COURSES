from statistics import mean

with open('13_9_9740.txt') as file:
    cnt = 0
    for s in file:
        lst = list(map(int, s.split()))
        l_rep = list(filter(lambda x: lst.count(x) > 1, lst))
        l_fr = list(filter(lambda x: lst.count(x) == 1, lst))
        if len(l_rep) == 3 and len(set(l_rep)) == 1 and mean(l_fr) <= l_rep[0]:
            cnt += 1
            print(*lst)
print('---' * 10)
print(cnt)
