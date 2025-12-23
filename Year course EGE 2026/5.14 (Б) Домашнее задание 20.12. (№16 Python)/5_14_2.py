from functools import lru_cache



@lru_cache(None)
def f(n: int):
    if n < 20: return n
    return (n - 6) * f(n - 7)


for i in range(19, 47872, 10): f(i)

print((f(47872) - 290 * f(47865)) // f(47858))

# from functools import lru_cache
#
#
# @lru_cache(None)
# def f(n: int):
#     if n < 20: return n
#     return 2 * n * f(n - 4)
#
#
# for i in range(4, 13766, 10): f(i)
#
# print((f(13766) - 9 * f(13762)) // f(13758))
