with open('15_9_9832.txt') as file:
    for s in file:
        lst = [int(x) for x in s.split()]
        l_rep = sorted((x for x in lst if lst.count(x) > 1))
        if len(l_rep) == 4 and len(set(l_rep)) == 2 and max(lst) not in l_rep:
            print(sum(lst))
            break
