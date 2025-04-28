_str = input().split()
for i, char in enumerate(_str):
    if not i:
        count = 0
        res_lst = []
        res_lst.append([char])
    else:
        if _str[i -1] == char:
            res_lst[count].extend(char)
        else:
            res_lst.append([char])
            count += 1
print(res_lst)


# s = input().split()
# # кидаем первый символ в наш список, также удалив его из входного списка
# seq = [[s.pop(0)]]
#
# for c in s:
#     if c in seq[-1]:
#         seq[-1].append(c)
#     else:
#         seq.append([c])
#
# print(seq)