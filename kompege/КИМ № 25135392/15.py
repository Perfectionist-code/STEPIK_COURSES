# def f(x, y):
#     return (78125 != y + 4 * x) or ((A > x) and (A > y))
#
#
# for A in range(78000, 10 ** 10):
#     print(A,'!')
#     if all(f(x, y) for x in range(1, 100000) for y in range(1, 100000)):
#         print(A)
#         break

def f(x, y):
    return (87125 != y + 4 * x) or ((A > x) and (A > y))


for A in range(86120, 10 ** 10):
    print(A,'!')
    if all(f(x, y) for x in range(0, 100000) for y in range(0, 100000)):
        print(A)
        break