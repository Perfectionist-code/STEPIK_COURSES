alphabet_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

_str = input() + ' запретил букву'
for char in alphabet_ru:
    if char in _str:
        print(_str + ' ' + char)
        _str = ''.join(_str.replace(char, '')).strip().replace('  ', ' ')
