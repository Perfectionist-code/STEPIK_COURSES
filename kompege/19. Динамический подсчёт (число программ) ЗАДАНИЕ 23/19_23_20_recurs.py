from functools import lru_cache

d = set()


@lru_cache(None)
def f(curr, step):
    if step == 8:
        d.add(curr)
    else:
        f(curr + 1, step + 1)
        f(curr + 5, step + 1)
        f(curr * 3, step + 1)


f(1, 0)
# print(len(d))
cnt = 0
for num in d:
    if 1000 <= num <= 1024:
        cnt += 1
print(cnt)