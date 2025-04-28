# Подвиг 5. На вход программе подается строка с email-адресами, записанных через пробел. Нужно прочитать эту строку и среди email-адресов оставить только корректно записанные адреса. Полагается, что к таким относятся те, что используют только латинские буквы, цифры и символ подчеркивания. Также в адресе должен быть символ "@", а после него символ точки "." (между ними, конечно же, могут быть и другие символы).
#
# Результат отобразить в виде строки email-адресов, записанных через пробел в порядке их следования в исходной строке.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.4.5
#
# Sample Input:
#
# abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com
# Sample Output:
#
# abc@it.ru biba123@list.ru sc_lib@list.ru
# from string import ascii_lowercase, digits
#
#
def is_email_correct(email):
    true_chars = ascii_lowercase + digits + '_@.'
    previous_character = ''
    dog_index = 0
    dot_count = 0
    if email.count('@') > 1 and email.count('.') == 0:
        return False
    elif '.' in email[-2:-1] or '@' == email[0] or '.' == email[0]:
        return False
    elif email.index('.') < email.index('@'):
        return False
    for ind, char in enumerate(email):
        if char in true_chars:
            if char == '@':
                dog_index = ind
            if (previous_character == '@' and char == '.') or (previous_character == '.' and char == '@'):
                return False
            if previous_character == '.' and char == '.':
                return False
            if char == '.' and ind > dog_index:
                dot_count += 1
        else:
            return False
        previous_character = char
    if dot_count == 0:
        return False
    return True


email_lst = input().split()
correct_email = filter(is_email_correct, email_lst)
print(*correct_email)
