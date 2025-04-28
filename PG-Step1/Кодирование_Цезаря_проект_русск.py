from string import ascii_uppercase, ascii_lowercase
ascii_uppercase1 = ascii_uppercase * 2
ascii_lowercase1 = ascii_lowercase * 2
utf_8_ru_lowercase = ''.join([chr(x) for x in range(1072, 1104)]) * 2
utf_8_ru_uppercase = ''.join([chr(x) for x in range(1040, 1072)]) * 2
# print(utf_8_ru_lowercase)


def crypt_message(message: str, shift = 10, shift_direction = 'right'):
    crypted_msg = []
    len_utf_8 = len(utf_8_ru_lowercase)
    for char in message:
        if char in utf_8_ru_lowercase or char in utf_8_ru_uppercase:
            char_idx = utf_8_ru_lowercase.find(char.lower())
        if char in ascii_lowercase or char in ascii_uppercase:
            char_idx = ascii_lowercase.find(char.lower())
        if char in utf_8_ru_uppercase:
            crypted_msg.append(utf_8_ru_uppercase[char_idx + shift if shift_direction == 'right' else char_idx - shift])
        elif char in utf_8_ru_lowercase:
            crypted_msg.append(utf_8_ru_lowercase[char_idx + shift if shift_direction == 'right' else char_idx - shift])
        elif char in ascii_uppercase1:
            crypted_msg.append(ascii_uppercase1[char_idx + shift if shift_direction == 'right' else char_idx - shift])
        elif char in ascii_lowercase1:
            crypted_msg.append(ascii_lowercase1[char_idx + shift if shift_direction == 'right' else char_idx - shift])
        else:
            crypted_msg.append(char)
    return ''.join(crypted_msg)


# print('*' * 10, 'Программа шифрования алгоритмом Цезаря', '*' * 10)
# message = input('Введите текст для шифрования: ')
# shift = int(input('Введите сдвиг шифрования '))
# direction = input('Введите направление шифрования (right/left) ')

# print(crypt_message(message, shift = shift, shift_direction = direction))

for i in range(1, 25):
    print(crypt_message('Hawnj pk swhg xabkna ukq nqj.', shift = -i))


