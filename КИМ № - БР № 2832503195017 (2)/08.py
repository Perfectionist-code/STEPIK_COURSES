from string import printable

cnt = 0
cnt1 = 0
for x in printable[1:13]:
    for y in printable[:13]:
        for z in printable[:13]:
            num = f'{x}{y}{z}'
            n = num
            for char in '13579b':
                num = num.replace(char, '*')
            if '**' not in num and cnt % 10 == 7:
                print(f'{cnt}: {n}')
                cnt1 += 1
            cnt += 1
print(cnt1)
