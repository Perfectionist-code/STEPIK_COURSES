with open('9.txt') as file:
    cnt = 0
    for s in file:
        lst = sorted(map(int, s.split()))
        lst_rep = [x for x in lst if lst.count(x) > 1]
        lst_fr = sorted([x for x in lst if lst.count(x) == 1])
        max_lst = max(lst)
        if max_lst in lst_rep and len(lst_rep) in (3, 4) and len(set(lst_rep)) == 1:
            if lst_fr[0] + lst_fr[-1] <= sum(lst_fr[1:-1]):
                cnt += 1
                print(*lst)
print(cnt)
