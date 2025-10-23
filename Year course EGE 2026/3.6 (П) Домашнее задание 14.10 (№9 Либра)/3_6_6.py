from collections import Counter


def cond_1(l: list) -> bool:
    _counter = Counter(l)
    cnt_repeat = 0
    cnt_not_repeat = 0
    sum_rep = 0
    sum_n_rep = 0
    for key, value in _counter.items():
        if value == 1:
            cnt_not_repeat += 1
            sum_n_rep += key
        if value > 1:
            cnt_repeat += 1
            sum_rep += value * key
    return cnt_repeat > 0 and cnt_not_repeat > 0 and l.count(max(l)) == 1 and sum_n_rep >= 3 * sum_rep


with open('06.txt') as file:
    cnt = 0
    for s in file:
        lst = list(map(int, s.split()))
        if cond_1(lst):
            cnt += 1
            print(*lst)
print('-----' * 5)
print(cnt)