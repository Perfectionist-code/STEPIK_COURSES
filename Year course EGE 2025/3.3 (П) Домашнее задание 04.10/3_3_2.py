with open('DZ_HL.txt', 'r') as file:
    lst = [int(x) for x in file]
    print(lst)
    cnt = 0
    a = lst[0]
    for i in range(1, lst.__len__()):
        b = lst[i]
        max_ab = max(a, b)
        min_ab = min(a, b)
        if all([a > 0 and b > 0, max_ab > 2 * min_ab]):
            cnt += 1
            print(a, b)
        a = b
print('Ответ:', cnt)
