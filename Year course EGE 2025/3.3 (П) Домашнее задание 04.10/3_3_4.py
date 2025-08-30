with open('DZ_HL.txt', 'r') as file:
    lst = [int(x) for x in file]
    a = lst[0]
    res_lst = []
    for i in range(1, lst.__len__() - 1):
        b = lst[i]
        c = lst[i + 1]
        if any([9 < abs(a) < 100 and 9 < abs(b) < 100, 9 < abs(b) < 100 and 9 < abs(c) < 100,
                9 < abs(c) < 100 and 9 < abs(a) < 100]):
            print((tup := (a, b, c)))
            res_lst.extend(tup)
            print(res_lst)
        a = b
print('Ответ:', sum(res_lst))
