mask = '255.255.254.0'
mask = '.'.join((f'{x:>08b}' for x in map(int, mask.split('.'))))
print(mask)
i = mask.count('0')
print('Ответ:', 2 ** i - 2)
