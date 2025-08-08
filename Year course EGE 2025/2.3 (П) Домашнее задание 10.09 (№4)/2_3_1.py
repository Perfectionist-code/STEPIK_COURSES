from itertools import product
codes = sorted(['1', '00', '010', '0110', '01110', '011110', '0111110'])
for code_i in product('01', repeat=8):
    code_i = ''.join(code_i)
    for code in codes:
        if code_i.startswith(code) or code.startswith(code_i):
            break
    else:
        print(code_i, 'pass')


