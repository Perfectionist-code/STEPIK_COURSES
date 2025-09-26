from string import digits, ascii_lowercase

d = {i: x for i, x in enumerate(digits + ascii_lowercase)}


def num_to_cs(num, cs):
    res = []
    while num:
        num, r = divmod(num, cs)
        res.append(d[r])
    return ''.join(res[::-1])


cnt = 0
for n in range(1, 1000):
    try:
        if num_to_cs(n, 5).__len__() <= 4 and num_to_cs(n, 2).__len__() >= 5 and num_to_cs(n, 16).endswith('c'):
            cnt += 1
            print(n)
    except:
        continue
print(cnt)
