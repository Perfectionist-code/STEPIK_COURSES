with open('23_24_11954.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 100_000
for l in range(ls):
    for r in range(l + m, l, -1):
        c = s[l:r + 1]
        if c.count('X') >= 500:
            if 'Y' not in c:
                m = min(m, len(c))
                print(c)
            else:
                break

        # else:
        #     break
print(m)

# m = 0
# res = []
# for l in range(ls):
#     for r in range(l + m, ls):
#         c = s[l:r + 1]
#         if 'Y' not in c:
#             if c.count('X') >= 500:
#                 m = max(m, len(c))
#                 # print(c)
#                 res.append(c)
#             # else:
#             #     break
#         else:
#             break
# print(len(res), len(min(res, key=len)))
# print(min(res, key=len))
# print(m)
