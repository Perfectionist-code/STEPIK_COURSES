from random import sample, shuffle, randint

friends_lst = [input() for _ in range(int(input()))]
friends_lst_copy = friends_lst.copy()
shift = randint(1, len(friends_lst) - 1)
for i, name in enumerate(friends_lst):
    print(name, '-', friends_lst[i-shift])



# import random
#
# a = [input() for _ in range(int(input()))]
# ln = len(a)
# b = [i for i in range(ln)]
# c = [i for i in range(ln)]
# random.shuffle(c)
# cnt = 1
# while True:
#     flag = 0
#     for i in range(ln):
#         if b[i] == c[i]:
#             flag += 1
#     if flag == 0:
#         break
#     else:
#         random.shuffle(c)
#         cnt += 1
#
# for n in range(ln):
#     print(f'{a[n]} - {a[c[n]]}')
#
# print(cnt)
