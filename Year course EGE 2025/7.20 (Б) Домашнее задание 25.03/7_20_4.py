with open('04.txt') as file:
    lst = [int(x) for x in file]
min_el_end = str(min(lst))[-1]
res = []
for tr in zip(lst, lst[1:], lst[2:]):
    l_neg = len([x for x in tr if x < 0])
    l_pos = len([x for x in tr if x > 0])
    if l_neg > l_pos and str(sum(tr))[-1] == min_el_end:
        res.append(abs(sum(tr)))
print(len(res), max(res))
