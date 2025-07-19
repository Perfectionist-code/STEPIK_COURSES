with open('o_17_2.txt', 'r') as file:
    lst = []
    cnt = 0
    max_sum = -1e10
    for line in file:
        lst.append(int(line))
    min_element = min(lst)
    a = lst[0]
    for i in range(1, len(lst)):
        b = lst[i]
        if a % 117 == min_element or b % 117 == min_element:
            cnt += 1
            if (element_summ:=(a + b)) > max_sum:
                max_sum = element_summ
        a = b
print(cnt, max_sum)
