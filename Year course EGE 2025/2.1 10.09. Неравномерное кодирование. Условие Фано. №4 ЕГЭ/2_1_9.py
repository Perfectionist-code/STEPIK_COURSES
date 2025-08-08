from itertools import product
codes = sorted(['1001', '11', '0', '101'])
for code_i in product('01', repeat=5):
    code_i = ''.join(code_i)
    for code in codes:
        if code_i.startswith(code) or code.startswith(code_i):
            break
    else:
        print(code_i, 'pass')


