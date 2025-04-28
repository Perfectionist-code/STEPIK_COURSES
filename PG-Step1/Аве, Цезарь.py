from string import ascii_uppercase, ascii_lowercase, punctuation

ascii_uppercase1 = ascii_uppercase * 2
ascii_lowercase1 = ascii_lowercase * 2
utf_8_ru_lowercase = ''.join([chr(x) for x in range(1072, 1104)]) * 2
utf_8_ru_uppercase = ''.join([chr(x) for x in range(1040, 1072)]) * 2


def crypt_message(message: str, shift=0):
    crypted_msg = []
    for char in message:
        if char in utf_8_ru_lowercase or char in utf_8_ru_uppercase:
            char_idx = utf_8_ru_lowercase.find(char.lower())
        if char in ascii_lowercase or char in ascii_uppercase:
            char_idx = ascii_lowercase.find(char.lower())
        if char in utf_8_ru_uppercase:
            crypted_msg.append(utf_8_ru_uppercase[char_idx + shift])
        elif char in utf_8_ru_lowercase:
            crypted_msg.append(utf_8_ru_lowercase[char_idx + shift])
        elif char in ascii_uppercase1:
            crypted_msg.append(ascii_uppercase1[char_idx + shift])
        elif char in ascii_lowercase1:
            crypted_msg.append(ascii_lowercase1[char_idx + shift])
        else:
            crypted_msg.append(char)
    return ''.join(crypted_msg)


def count_shift(message_element: str):
    cnt = 0
    for ch in message_element:
        if ch in punctuation:
            cnt += 1
    return len(message_element) - cnt


def crypt_ave_cesar(mess: str):
    message_lst = mess.split()
    ave_cesar_msg = []
    for msg_el in message_lst:
        ave_cesar_msg.append(crypt_message(msg_el, shift = count_shift(msg_el)))
    return ' '.join(ave_cesar_msg)


# print('*' * 10, 'Программа шифрования алгоритмом Цезаря', '*' * 10)
# message = input('Введите текст для шифрования: ')
# shift = int(input('Введите сдвиг шифрования '))
# direction = input('Введите направление шифрования (right/left) ')

# print(crypt_message(message, shift = shift, shift_direction = direction))
message = input()

print(crypt_ave_cesar(message))
# for i in range(1, 25):
#     print(crypt_message('Hawnj pk swhg xabkna ukq nqj.', shift = -i))
