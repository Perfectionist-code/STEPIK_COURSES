from collections import Counter

# lst = [x.strip('.,!?:;-') for x in input().lower().split()]
# # res = Counter(lst)
# res_lst = []
# # for key in res:
# #     if res[key] == min(res.values()):
# #         res_lst.append(key)
# # print(min(res_lst))



lst = [x.strip('.,!?:;-') for x in input().lower().split()]
res_d = {}
for word in set(lst):
    res_d.setdefault(lst.count(word),[]).append(word)
print(min(res_d[min(res_d)]))


# d = {}
# for w in input().split():
#     w = w.strip('.,!?:;-').lower()
#     d[w] = d.get(w, 0) + 1
# print(min(d.items(), key=lambda x: (x[1], x[0]))[0])


# st = [i.strip('.,!?:;-') for i in input().lower().split()]
#
# print(min(st, key=lambda x: (st.count(x), x)))