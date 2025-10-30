with open('16_09_8609.txt') as file:
    cnt = 0
    for s in file:
        lst = sorted(map(int, s.split()))
        if len(set(lst)) == len(lst) and 2 * (lst[0] + lst[-1]) <= 3 * sum(lst[1:-1]):
            cnt += 1
print(cnt)
