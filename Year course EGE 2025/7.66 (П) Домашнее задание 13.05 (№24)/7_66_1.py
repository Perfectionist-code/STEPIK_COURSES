from re import finditer

with open('01_24-337.txt') as file:
    s = file.readline()
print((ls := len(s)))

num = r'1([A-D]|[0-9])*[07]'
reg = fr'(?=({num}))'
m = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(m), m)

# m = 0
# for l in range(ls):
#     for r in range(l + m, ls):
#         c = s[l: r + 1]
#         if c.startswith('1'):
#             if all(x in '0123456789ABCD' for x in c) and int(c, 14) % 7 == 0:
#                 m = max(m, len(c))
#                 print(c)
#         else:
#             break
# print(m)


# 1229877786657664736677663764600366363865863563866630767637767633003030
# 12298777866576647366776637646003663638658635638666630767637767633013030