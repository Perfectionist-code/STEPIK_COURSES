# from string import digits, ascii_lowercase
#
# d = {i: x for i, x in enumerate(digits + ascii_lowercase)}
# d2 = {x: i for i, x in enumerate(digits + ascii_lowercase)}
#
# def num_to_cs(num, cs):
#     res = []
#     while num:
#         num, r = divmod(num, cs)
#         res.append(d[r])
#     return ''.join(res[::-1])
#
#
# def cond3(n) -> bool:
#     for i in range(len(n) - 1):
#         if bool(int(d2[n[i]]) % 2) == bool(int(d2[n[i + 1]]) % 2):
#             return False
#     return True
#
#
# cnt = 0
# for i in range(1000000):
#     num = num_to_cs(i, 13)
#     if len(num) == 5 and num.count('2') == 1 and cond3(num):
#         cnt += 1
#         print(num)
# print('-----' * 5)
# print('Ответ:', cnt)

def num_to_cs(n, cs):
    res = []
    while n:
        n, r = divmod(n, cs)
        res.append(r)
    return res[::-1]


def cond3(n) -> bool:
    for i in range(len(n) - 1):
        if bool(n[i] % 2) == bool(n[i + 1] % 2):
            return False
    return True


cnt = 0
for i in range(10000, 1000000):
    num = num_to_cs(i, 13)
    if len(num) == 5 and num.count(2) == 1 and cond3(num):
        cnt += 1
print('Ответ:', cnt)