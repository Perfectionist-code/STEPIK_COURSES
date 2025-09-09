mask = '255.255.240.0'
mask = '.'.join((f'{x:>08b}' for x in map(int, mask.split('.'))))
i = mask.count('0')
print('Ответ:', 2 ** i - 2)
