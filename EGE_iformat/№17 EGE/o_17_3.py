with open('o_17_3.txt', 'r') as file:
    lst = []
    cnt = 0
    max_sum = -1e10
    for line in file:
        lst.append(int(line))
    a = lst[0]
    b = lst[1]
    for i in range(2, len(lst)):
        c = lst[i]
        if not ((a * b * c) % 7) and sum((a, b, c)) % 10 == 5:
            cnt += 1
            if (element_summ:=(a + b + c)) > max_sum:
                max_sum = element_summ
        a = b
        b = c
print(cnt, max_sum)
