m = int(input())
n = int(input())
books_in_library = [input() for _ in range(m)]
books_in_list = [input() for _ in range(n)]
res = set(books_in_list).intersection(books_in_library)
res_lst = []
for book in books_in_list:
    if book in res:
       res_lst.append('YES')
    else:
        res_lst.append('NO')
print(*res_lst,sep = '\n')



# m, n = int(input()), int(input())
# libr = {input() for _ in range(m)}
#
# for _ in range(n):
#     if input() in libr:
#         print('YES')
#     else:
#         print('NO')