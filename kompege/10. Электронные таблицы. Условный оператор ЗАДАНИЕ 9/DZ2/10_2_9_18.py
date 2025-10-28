with open('18_09_10910.txt') as file:
    cnt = 0
    for s in file:
        lst = sorted(map(int, s.split()))
        l_rep = [x for x in lst if lst.count(x) > 1]
        if min(lst) not in l_rep and l_rep and min(lst) + max(lst) < sum(l_rep):
            cnt += 1
print(cnt)
