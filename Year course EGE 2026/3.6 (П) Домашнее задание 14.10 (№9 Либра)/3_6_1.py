def cond_1(l: list) -> bool:
    l = sorted(l, key=lambda x: (l.count(x), x), reverse=True)
    if len(set(l)) == len(l) - 2 and l[0] == l[1] == l[2]:
        return True
    return False


def cond_2(l: list) -> bool:
    return all((l[i] <= l[i + 1] for i in range(len(l) - 1)))


with open('01.txt') as file:
    cnt = 0
    for s in file:
        lst = list(map(int, s.split()))
        if (cond_1(lst) + cond_2(lst)) <= 1:
            cnt += 1
            print(*lst)
print('----' * 5)
print(cnt)
