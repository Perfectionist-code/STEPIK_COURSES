n = int(input())
lst = [[int(x) for x in input().split()] for _ in range(n)]
print(sum(lst[i][j] for i in range(n) for j in range(n) if i == j))


# n = int(input())
# sm = 0
#
# for i in range(n):
#     cur_seq = input().split()
#     sm += int(cur_seq[i])
#
# print(sm)