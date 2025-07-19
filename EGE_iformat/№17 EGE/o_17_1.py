with open('o_17_1.txt', 'r') as file:
    lst = []
    cnt = 0
    min_prod = 1e10
    for line in file:
        lst.append(int(line))
    a = lst[0]
    for i in range(1, len(lst)):
        b = lst[i]
        if (pr := a * b) > 0 and not ((a + b) % 7):
            cnt += 1
            if pr < min_prod:
                min_prod = pr
        a = b
print(cnt, min_prod)
