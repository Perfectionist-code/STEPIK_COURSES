from itertools import product

codes = sorted(['00', '1000', '010', '011', '1011', '1001', '1100', '1010', '1101'])
for code_i in product('01', repeat=3):
    code_i = ''.join(code_i)
    for code in codes:
        if code_i.startswith(code) or code.startswith(code_i):
            break
    else:
        print(code_i, 'pass')
