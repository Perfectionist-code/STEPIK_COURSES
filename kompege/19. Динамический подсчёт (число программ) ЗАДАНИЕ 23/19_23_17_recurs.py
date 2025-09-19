from functools import lru_cache


# @lru_cache(None)
def f(curr, end):
    if curr > end: return 0
    if curr == end: return 1
    return f(curr + 2, end) + f(curr + 4, end) + f(curr + 5, end)


for i in range(32, 300):
    if f(31, i) == 1001:
        print(i)
        break
