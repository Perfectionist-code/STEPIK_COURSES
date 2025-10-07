def cond_1(l: list) -> bool:
    return len(set(l)) == len(l)


def cond_2(l: list) -> bool:
    return 3 * (l[0] + l[-1]) >= 2 * sum(l[1:-1])


with open('7_11_6.txt', 'r') as file:
    cnt = 0
    for s in file:
        lst = sorted(map(int, s.split()))
        if cond_1(lst) and cond_2(lst):
            cnt += 1
print('Ответ:', cnt)
