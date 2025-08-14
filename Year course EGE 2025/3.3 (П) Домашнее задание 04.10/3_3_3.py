with open('DZ_HL.txt', 'r') as file:
    lst = [int(x) for x in file]
    a = lst[0]
    res_lst = []
    for i in range(1, lst.__len__() - 1):
        b = lst[i]
        c = lst[i + 1]
        if all([a > 0, b > 0, c > 0]):
            print((tup := (a, b, c)), min_tup := min(tup))
            res_lst.append(min_tup)
        a = b
print(min(res_lst))
