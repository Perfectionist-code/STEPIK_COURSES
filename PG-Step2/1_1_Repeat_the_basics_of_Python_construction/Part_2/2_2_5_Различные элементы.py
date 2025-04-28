lst, product = [int(x) for x in (input() for _ in range(int(input())))], int(input())
flag = False
for i in range(len(lst) - 1):
    for j in range(i + 1, len(lst)):
        if lst[i] * lst[j] == product:
            flag = True
    if flag:
        break
print(('НЕТ', 'ДА')[flag])
