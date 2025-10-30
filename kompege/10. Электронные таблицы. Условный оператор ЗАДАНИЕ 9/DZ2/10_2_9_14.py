from statistics import mean

with open('14_09_9778.txt') as file:
    for i, s in enumerate(file, 1):
        lst = list(map(int, s.split()))
        l_rep = [x for x in lst if lst.count(x) > 1]
        l_fr = [x for x in lst if lst.count(x) == 1]
        if len(l_rep) == 2 and mean(l_fr) <= l_rep[0]:
            print(i)
            break
