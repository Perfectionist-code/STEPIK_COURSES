from statistics import mean

with open('11_9_5126.txt') as file:
    cnt = 0
    for s in file:
        lst = list(map(int, s.split()))
        l_rep = [x for x in lst if lst.count(x) > 1]
        l_fr = [x for x in lst if lst.count(x) == 1]
        if len(l_rep) == 3 and len(set(l_rep)) == 1 and mean(l_fr) <= sum(l_rep):
            print(*lst)
            cnt += 1
print('-----' * 5)
print(cnt)
