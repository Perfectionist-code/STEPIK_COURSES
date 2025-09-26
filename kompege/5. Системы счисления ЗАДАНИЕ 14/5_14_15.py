def num_to_cs(num, cs):
    res = []
    while num:
        num, r = divmod(num, cs)
        res.append(str(r))
    return ''.join(res[::-1])


for x in range(21, 30):
    if num_to_cs(x, 3).endswith('11'):
        print(x)
        break
