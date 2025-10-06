from itertools import permutations


def condition_1(l: list) -> bool:
    return l[0] < sum(l[1:])


def condition_2(l: list) -> bool:
    for per in permutations(l):
        a, b, c, d = per
        if a + b == c + d:
            return True
    return False


with open('7_11_5.txt', 'r') as file:
    cnt = 0
    for s in file:
        lst = sorted(map(int, s.split()), reverse=True)
        if condition_1(lst) and condition_2(lst):
            cnt += 1
            print(*lst)
print('------' * 5)
print('Ответ:', cnt)
