cnt = 0
while (num := input()) != 'СТОП':
    if (num := int(num)) < 0 and num % 2:
        cnt += 1
print(cnt)