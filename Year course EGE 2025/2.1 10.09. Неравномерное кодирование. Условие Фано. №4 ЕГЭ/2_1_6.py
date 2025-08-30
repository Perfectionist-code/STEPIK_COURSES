from itertools import product
codes = sorted(['10', '110', '01', '001', '111'])
# code_i = input()
for code_i in product('01', repeat=4):
    code_i = ''.join(code_i)
    for code in codes:
        if code_i.startswith(code) or code.startswith(code_i):
            break
    else:
        print(code_i, 'pass')


