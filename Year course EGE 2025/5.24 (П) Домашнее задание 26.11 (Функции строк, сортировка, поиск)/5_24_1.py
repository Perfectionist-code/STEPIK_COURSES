# from collections import Counter
#
# lst = list(map(int, input().split()))
# _counter = Counter(lst)
# print(_counter)
# res = int(10e26)
# max_counter = 0
# for num, count in _counter.items():
#     if count >= max_counter:
#         max_counter = count
#         if res > num:
#             res = num
# print(max_counter, res)

lst = sorted(map(int, input().split()))
lst = sorted(lst, key=lambda x: lst.count(x), reverse=True)
print(*lst)
print(lst[0])

# 0 1 3 5 0 2 2 4 2 3 0
# 0 1 3 5 0 2 2 4 2 3 0 1 1 1
# 0 1 3 5 0 2 2 4 2 3 0 1 1 1 0