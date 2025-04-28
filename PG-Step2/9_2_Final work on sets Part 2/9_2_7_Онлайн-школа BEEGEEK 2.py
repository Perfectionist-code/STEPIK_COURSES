m, n = int(input()), int(input())
set_1 = {input() for _ in range(m)}
set_2 = {input() for __ in range(n)}
print(len(set_1 - set_2))


# m, n = [int(input()) for _ in range(2)]
#
# math = {input() for _ in range(m)}
# informatics = {input() for _ in range(n)}
#
# only_math = math - informatics
# print(len(only_math))