from itertools import product
codes = sorted(['000', '001', '0101', '0100', '011'])
for code_i in product('01', repeat=3):
    code_i = ''.join(code_i)
    for code in codes:
        if code_i.startswith(code) or code.startswith(code_i):
            break
    else:
        print(code_i, 'pass')


