from itertools import product

cnt = 0
for pr in product("01234", repeat=6):
    word = "".join(pr).lstrip('0')
    if all((len(word)==6,not word.startswith("1"), not word.endswith("3"), not word.endswith("4"))):
        print(word)
        cnt += 1

print(cnt)
