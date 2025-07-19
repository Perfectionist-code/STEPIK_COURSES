from itertools import product

cnt = 0
for prod in product('ДИОНС', repeat=5):
    prod = ''.join(prod)
    gl_cnt = sg_cnt = 0
    for char in 'ДНС':
        sg_cnt += prod.count(char)
    for char in 'ИО':
        gl_cnt += prod.count(char)
    if sg_cnt <= gl_cnt:
        print(prod)
        cnt += 1
print()
print(cnt)
