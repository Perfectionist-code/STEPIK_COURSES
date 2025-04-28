# Подвиг 3. Объявите в программе функцию с именем check_password, которая первым параметром принимает строку (пароль) и имеет второй формальный параметр chars с начальным значением в виде строки "$%!?@#". Функция должна проверять, есть ли в пароле хотя бы один символ из chars и что длина пароля не менее 8 символов. Если проверка проходит, то функция возвращает булево True, иначе False.
#
# P. S. Вызывать функцию не нужно, только объявить.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.4.3
#
# Sample Input:
#
# 12345678!
# Sample Output:
#
# True

def check_password(password,chars="$%!?@#") :
    """
    The function of verifying the correctness of the entered password.
    :param password: lue - string, password
    :param chars: string (formal parameter), the presence of at least one mandatory character from $%!?@#
    :return: True, если длинна пароля не менее 8 символов и содержит хотя бы один символ из $%!?@#. Иначе возвращает Ложь
    """
    if len(password) >= 8 :
        password_set = {char for char in password}
        chars_set = {char for char in chars}
        # print(password_set & chars_set)
        return password_set & chars_set != set()
    return False


passw = input()
print('Password OK' if check_password(passw) else 'The password does not meet the required criteria')
