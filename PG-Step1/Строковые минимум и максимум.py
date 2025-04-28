_str = input()
lst = []
while _str != 'КОНЕЦ':
    lst.append(_str)
    _str = input()
print(f'Минимальная строка ⬇️: {min(lst)}\n'
      f'Максимальная строка ⬆️: {max(lst)}')
