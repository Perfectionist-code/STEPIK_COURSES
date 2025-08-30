from itertools import product
codes = sorted(['11', '101', '010', '00'])
for code_i in product('01', repeat=3):
    code_i = ''.join(code_i)
    for code in codes:
        if code_i.startswith(code) or code.startswith(code_i):
            break
    else:
        print(code_i, 'pass')


