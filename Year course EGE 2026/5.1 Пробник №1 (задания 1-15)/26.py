f = open('26.txt')
N = int(f.readline())
a = []
for s in f:
    art, m, st = [int(el) for el in s.split()]
    a.append([art, m, st])

sred_sum = sum([x[1] for x in a]) / len(a)
a = [x for x in a if x[1] > sred_sum]
dict_prod = dict()
for el in a:
    art, m, st = el
    dict_prod[art] = [m, 0, 0]
for el in a:
    art, m, st = el
    dict_prod[art][1] += st
    dict_prod[art][2] += (not (st))

max_st0 = max(x[2] for x in dict_prod.values())
posible_res = (x for x in dict_prod.values() if x[2] == max_st0)
result = min(posible_res, key=lambda x: (x[0],x[1]))
print(result[0] * result[2], result[1])



# list_answ = dict_prod[31218]
# for el in dict_prod:
#     if dict_prod[el][2] > list_answ[2]:
#         list_answ = dict_prod[el]
#     elif dict_prod[el][2] == list_answ[2]:
#         if dict_prod[el][0] < list_answ[0]:
#             list_answ = dict_prod[el]
#         elif dict_prod[el][0] == list_answ[0]:
#             if dict_prod[el][1] < list_answ[1]:
#                 list_answ = dict_prod[el]
#
# print(list_answ[0] * list_answ[2])
# print(list_answ[1])
