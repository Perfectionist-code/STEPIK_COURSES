# with open('26var01.txt') as file:
#     n, g, v = map(int, file.readline().split())
#     a = []
#     for s in file:
#         gr, vr = map(int, s.split())
#         a.append((gr, vr))

with open('26var01_test.txt') as file:
    n, g, v = map(int, file.readline().split())
    a = []
    for s in file:
        gr, vr = map(int, s.split())
        a.append((gr, vr))

pole = [[0 for j in range(v)] for i in range(g)]
for gr, vr in a:
    # print(gr,vr)
    pole[gr - 1][vr - 1] = 1
    sum_c = 0
# for col in zip(*pole):
#     s = sum(col)
#     sum_c += s
# print(sum(col))
# print(sum_c)

# pole[1][3] = 1
print(*pole, sep='\n')
res = []
max_i = 0
for j in range(vr):
    for i in range(gr):
        if

