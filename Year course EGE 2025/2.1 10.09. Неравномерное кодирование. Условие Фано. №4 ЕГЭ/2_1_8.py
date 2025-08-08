from itertools import product
codes = sorted(['110', '01', '10', '000', '001'])
for code_i in product('01', repeat=4):
    code_i = ''.join(code_i)
    for code in codes:
        if code_i.startswith(code) or code.startswith(code_i):
            break
    else:
        print(code_i, 'pass')


