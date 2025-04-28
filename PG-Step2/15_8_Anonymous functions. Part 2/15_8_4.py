is_num = lambda x: all([y in '0123456789.' for y in x.replace('-','', 1)]) and x.count('.')  <= 1 and '-' not in x[1:]


print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))