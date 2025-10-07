from itertools import permutations


def cond_1(l: list) -> bool:
    return l[0] < sum(l[1:])


def cond_2(l: list) -> bool:
    for per in permutations(l):
        a, b, c, d = per
        if a + b == c + d:
            return False
    return True


with open('7_11_8.txt', 'r') as file:
    cnt = 0
    for s in file:
        lst = sorted(map(int, s.split()), reverse=True)
        if cond_1(lst) and cond_2(lst):
            cnt += 1
            print(*lst)
print('Ответ:', cnt)
