from statistics import mean

with open('3_22_5.txt', 'r') as file:
    for i, s in enumerate(file, 1):
        lst = list(map(int, s.split()))
        lst = sorted(lst, key=lambda x: (lst.count(x), x), reverse=True)
        if (len(set(lst)) == len(lst) - 1) and (lst[0] >= mean(lst[2:])):
            print(*lst)
            print('Ответ:', i)
            break
