with open('DZ_HL.txt', 'r') as file:
    lst = [int(x) for x in file]
    print(lst)
    cnt = 0
    a = lst[0]
    for i in range(1, lst.__len__()):
        b = lst[i]
        if any([a < 0 and not b < 0, b < 0 and not a < 0]):
            cnt += 1
            print(a, b)
        a = b
print('Ответ:', cnt)
