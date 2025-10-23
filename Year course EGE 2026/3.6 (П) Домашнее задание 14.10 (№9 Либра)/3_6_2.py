with open('02.txt') as file:
    cnt = 0
    for s in file:
        lst = sorted(map(int, s.split()))
        if len(set(lst)) == len(lst) - 1 and lst[0] != lst[1] and lst[-2] != lst[-1]:
            print(*lst)
            cnt += 1
print('----' * 5)
print(cnt)
