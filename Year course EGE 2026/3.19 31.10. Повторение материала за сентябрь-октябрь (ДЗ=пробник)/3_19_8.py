from statistics import mean

with open('08.txt') as file:
    for i, s in enumerate(file, 1):
        lst = list(map(int, s.split()))
        l_rep = [x for x in lst if lst.count(x) == 3]
        l_fr = [x for x in lst if lst.count(x) == 1]
        if len(l_rep) == 3 and len(set(l_rep)) == 1 and len(l_fr) == 3 and l_rep[0] > mean(l_fr):
            print(f'{i}:', *lst)
