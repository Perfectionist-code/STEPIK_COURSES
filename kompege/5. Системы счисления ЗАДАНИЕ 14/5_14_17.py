from string import digits, ascii_lowercase

d = {i: x for i, x in enumerate(digits + ascii_lowercase)}


def num_to_cs(num, cs):
    res = []
    while num:
        num, r = divmod(num, cs)
        res.append(d[r])
    return ''.join(res[::-1])

for n in range(2, 1000):
    try:
        if (l:=num_to_cs(68, n)).endswith('2') and l.__len__() == 4:
            print(n)
            break
    except:
        continue