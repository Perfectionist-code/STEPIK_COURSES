with open('ledger.txt', encoding = 'UTF-8') as file:
    _sum = 0
    for line in file:
        _sum += int(line.strip('$\n'))
print(f'${_sum}')
