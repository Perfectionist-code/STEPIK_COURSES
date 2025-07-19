max_prod = 0
for n in range(4, 1000):
    s = '9' + '3' * n
    while any(('22' in s, '333' in s, '9999' in s)):
        if '22' in s:
            s = s.replace('22', '3', 1)
        elif '333' in s:
            s = s.replace('333', '99', 1)
        else:
            s = s.replace('9999', '22', 1)
    prod_nums = 1
    for num in s:
        prod_nums *= int(num)
    if prod_nums > max_prod:
        max_prod = prod_nums
print(max_prod)
