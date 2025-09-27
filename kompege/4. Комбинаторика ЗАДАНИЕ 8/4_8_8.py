from itertools import product
from collections import Counter

cnt = 0
for pr in product("123AB", repeat=8):
    _counter = Counter(pr)
    if sum((_counter["A"], _counter["B"])) == 2:
        cnt += 1
print(cnt)
