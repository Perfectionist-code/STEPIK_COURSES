from string import digits, ascii_lowercase

d = {i: x for i, x in enumerate(digits + ascii_lowercase)}
for x in range(15):
    num1 = int(n1 := f'123{d[x]}5', 15)
    num2 = int(n2 := f'1{d[x]}233', 15)
    if not ((num1 + num2) % 14):
        print((num1 + num2) // 14)
        break
