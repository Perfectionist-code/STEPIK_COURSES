n, cnt, new_num = list(input()), 0, []
for x in n[::-1]:
    cnt += 1
    if cnt == 3:
        new_num.append(x)
        new_num.append(',')
        cnt = 0
    else:
        new_num.append(x)
print(''.join(new_num[::-1]).lstrip(','))

# num = input()
# for idx in range(len(num) - 3, 0, -3):
#     num = num[:idx] + ',' + num[idx:]
# print(num)