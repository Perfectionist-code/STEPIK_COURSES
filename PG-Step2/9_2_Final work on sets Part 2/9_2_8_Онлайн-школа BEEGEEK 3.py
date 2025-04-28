m, n = int(input()), int(input())
set_1 = {input() for _ in range(m)}
set_2 = {input() for __ in range(n)}
res = len(set_1.symmetric_difference(set_2))
print(('NO', res)[bool(res)])


# m, n = int(input()), int(input())
# math = {input() for _ in range(m)}
# inf = {input() for _ in range(n)}
# result = len(math ^ inf)
#
# if result:
#     print(result)
# else:
#     print('NO')