lst = input().split()
n = int(input())
res = []
temp_lst = []
for i in range(n):
    for j in range(i, len(lst), n):
        temp_lst.append(lst[j])
    res.append(temp_lst)
    temp_lst = []
print(res)

# symbols = input().split()
# n = int(input())
# result = [[] for _ in range(n)]
#
# for i in range(len(symbols)):
#     result[i % n].append(symbols[i])
#
# print(result)

# s = input().split()
# n = int(input())
# res = []
# for i in range(n):
#     res.append(s[i::n])
# print(res)