def cond1(l: list) -> bool:
    return (l[0] + l[-1]) ** 2 > sum([x ** 2 for x in l[1:-1]])


def cond2(l: list) -> bool:
    l_rp = [x for x in l if l.count(x) > 1]
    # l_fr = [x for x in l if l.count(x) == 1]
    return len(l_rp) == 3 and len(set(l_rp)) == 1


with open('12_9_5284.txt') as file:
    cnt = 0
    for s in file:
        lst = sorted(map(int, s.split()))
        if cond1(lst) or cond2(lst):
            cnt += 1
print(cnt)
