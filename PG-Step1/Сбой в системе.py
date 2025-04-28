_str = input()
lst = []
while _str != 'КОНЕЦ':
    lst.append(_str)
    _str = input()
print(f'Минимальная строка ⬇️: {min(lst)}\n'
      f'Максимальная строка ⬆️: {max(lst)}')

# l = list(iter(input, "КОНЕЦ"))
# print(f'Минимальная строка ⬇️: {min(l)}\nМаксимальная строка ⬆️: {max(l)}')