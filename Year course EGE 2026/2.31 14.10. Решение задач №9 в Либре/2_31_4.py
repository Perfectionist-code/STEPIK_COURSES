def condition_1(l: list) -> bool:
    return len(lst) == len(set(lst))


def condition_2(l: list) -> bool:
    return 2 * (lst[0] + lst[-1]) >= sum(lst[1:-1])


with open('04.txt') as file:
    cnt = 0
    for s in file:
        lst = sorted(map(int, s.split()), reverse=True)
        if condition_1(lst) and condition_2(lst):
            cnt += 1
            print(*lst)
print('----' * 5)
print(cnt)
