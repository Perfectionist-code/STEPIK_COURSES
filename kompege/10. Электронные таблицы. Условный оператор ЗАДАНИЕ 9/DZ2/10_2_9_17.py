from statistics import mean

with open('17_09_6357.txt') as file:
    cnt = 0
    for s in file:
        lst = [int(x) for x in s.split()]
        l_rep = [x for x in lst if lst.count(x) > 1]
        l_fr = [x for x in lst if lst.count(x) == 1]
        if l_rep and l_fr and mean(l_fr) < mean(l_rep):
            cnt += 1
print(cnt)
