def cond_1(l: list) -> bool:
    sum_even = sum((x for x in l if not x % 2))
    sum_odd = sum((x for x in l if x % 2))
    return sum_odd > sum_even


with open('03.txt') as file:
    cnt = 0
    for s in file:
        lst = list(map(int, s.split()))
        if (len(set(lst)) == len(lst) - 1) + cond_1(lst) == 1:
            cnt += 1
            print(*lst)
print('----' * 5)
print(cnt)
