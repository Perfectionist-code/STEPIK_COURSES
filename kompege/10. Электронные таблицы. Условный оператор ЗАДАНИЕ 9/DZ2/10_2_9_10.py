def cond1(l: list) -> bool:
    return l[-1] < sum(l[:-1])


def cond2(l: list) -> bool:
    return len(l) - 1 == len(set(l))


with open('10_9_4614.txt') as file:
    cnt = 0
    for s in file:
        lst = sorted(map(int, s.split()))
        if cond1(lst) and cond2(lst):
            print(*lst)
            cnt += 1
print('----' * 5)
print(cnt)
