with open('09.txt') as file:
    cnt = 0
    for s in file:
        lst = sorted(map(int, s.split()))
        min_n = min(lst)
        r_num = [x for x in lst if lst.count(x) > 1]
        fr_num = sorted([x for x in lst if lst.count(x) == 1])
        if min_n in r_num and len(r_num) in (2, 3) and len(set(r_num)) == 1 and fr_num[0] ** 2 + fr_num[-1] **2<= (sum(fr_num[1:-1]))**2:
            cnt += 1
            print(*lst)
print('----' * 5)
print(cnt)

# ОТВЕТ: 752