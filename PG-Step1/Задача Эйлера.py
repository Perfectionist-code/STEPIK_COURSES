# flag = True
# for a in range(1, 151):
#     if flag == False:
#         break
#     qa = a**5
#     for b in range(a, 151):
#         if flag == False:
#             break
#         qb = b**5
#         for c in range(b, 151):
#             if flag == False:
#                 break
#             qc = c**5
#             for d in range(c, 151):
#                 qd = d**5
#                 q_sum = qa + qb + qc + qd
#                 e = int(q_sum**0.2)
#                 if q_sum == e**5:
#                     print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")
#                     print(f"Их сумма - {a + b + c + d + e}")
#                     flag = False
#                     break

from datetime import datetime
start_time = datetime.now()

arr5 = [i ** 5 for i in range(2, 150)]                           # массив пятых степеней
abc = set(a + b + c for a in arr5 for b in arr5 for c in arr5)   # варианты сумм а^5+b^5+ c^5
de =  set(e - d  for e in arr5 for d in arr5 if e - d > 0)       # варианты разности е^5 - d^5
res = abc & de                                                   # пересечение вариантов

# находим a b c для верных ответов
abc_res = [[a + b + c, a, b, c] for a in arr5 for b in arr5 for c in arr5 if a + b + c in res]

# находим d e для верных ответов
de_res = [[e - d, e , d]  for e in arr5 for d in arr5 if (e - d in res) ]

elist = []
for i_res in res:            #  исключаем повторения
    for i_abc in abc_res:
        if i_res == i_abc[0]:
            aa, bb, cc = i_abc[1:]
    for i_de in de_res:
        if i_res == i_de[0]:
            ee, dd = i_de[1:]
    if ee not in elist:
        elist.append(ee)
        aa, bb, cc, dd, ee = sorted([round(aa**0.2), round(bb**0.2), round(cc**0.2), round(dd**0.2), round(ee**0.2)])
        print(aa, bb, cc, dd, ee,'a+b+c+d+e=',aa + bb + cc + dd + ee)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))