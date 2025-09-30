from string import digits, ascii_lowercase

d = {i: x for i, x in enumerate(digits + ascii_lowercase)}

for x in range(13):
    num1 = int(f'537{d[x]}623', 13)
    num2 = int(f'6{d[x]}35{d[x]}2', 13)
    if not (res := (num1 - num2)) % 3:
        print(x, res)
