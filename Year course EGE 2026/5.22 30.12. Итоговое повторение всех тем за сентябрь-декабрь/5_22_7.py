from itertools import product, repeat

cnt = 0
for pr in product('0123456', repeat=5):
    num = ''.join(pr)
    if not num.startswith('0') and num.count('6') == 1 and all(f'{x}{x}' not in num for x in '0123456'):
        print(num)
        cnt += 1
print('-----' * 5)
print(cnt)
