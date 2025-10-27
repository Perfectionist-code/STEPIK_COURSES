with open('07_9_4634.txt') as file:
    cnt = 0
    for s in file:
        lst = sorted(map(int, s.split()))
        if lst[0] * lst[-1] == lst[1] * lst[2] and lst[2] ** 2 > lst[0] * lst[-1]:
            cnt += 1
            print(*lst)
print('---' * 10)
print(cnt)
