from string import ascii_lowercase, digits
# d = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j', 20: 'k'}
d = {i: x for i, x in enumerate(digits+ascii_lowercase)}
divisor = 18
res_x = None
for x in range(21):
    x = d[x]
    for y in range(21):
        y = d[y]
        num1 = int(f'12{y}{x}9', 21)
        num2 = int(f'36{y}99', 21)
        res_num = num1 + num2
        if res_num % divisor:
            break
    else:
        res_x = x
        break
num1 = int(f'125{res_x}9', 21)
num2 = int(f'36599', 21)
res = (num1 + num2) // divisor
print(res)
