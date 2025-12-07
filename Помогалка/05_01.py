# https://education.yandex.ru/ege/inf/task/3ef214b5-fef2-4500-9f74-5be832f60ef6

def num_to_cs(num: int, cs):
    res = []
    while num:
        num, r = divmod(num, cs)
        res.append(str(r))
    return ''.join(res[::-1])


def get_r(num: int):
    r = num_to_cs(num, 5)
    if not len(r) % 2:
        r = list(r)
        r.insert(len(r) // 2, '0')
        r = ''.join(r)
    return int(r)

res = []
for n in range(1,10000):
    if (R:=get_r(n)) <= 250:
        res.append(n)
        print(n, R)
print('----' * 5)
print(max(res))
