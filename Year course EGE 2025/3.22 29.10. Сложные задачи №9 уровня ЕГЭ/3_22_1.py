def condition_1(lst_s: list) -> bool:
    return set(lst_s).__len__() == len(lst_s) - 1


def condition_2(lst_s: list) -> bool:
    sum_pos = 0
    sum_neg = 0
    for num in lst_s:
        if num > 0:
            sum_pos += num
        elif num < 0:
            sum_neg += num
    return abs(sum_neg) > sum_pos


with open('3_22_1.txt', 'r') as file:
    cnt = 0
    for s in file:
        lst = sorted(map(int, s.split()))
        if condition_1(lst) and condition_2(lst):
            print(*lst)
            cnt += 1
print(cnt)
