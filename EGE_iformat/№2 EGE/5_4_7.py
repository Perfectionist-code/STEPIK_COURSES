from itertools import product
res = 0
for per in product('0123456789', repeat=4):
    even_cnt = odd_cnt = 0
    for figure in per:
        if int(figure) % 2:
            odd_cnt += 1
        else:
            even_cnt += 1
    if odd_cnt == even_cnt:
        res += 1
print(res)
