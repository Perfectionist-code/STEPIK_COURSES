# Подвиг 8. Объявите в программе функцию с одним параметром, которая проверяет корректность переданного ей email-адреса в виде строки. Полагается, что адрес верен, если он обязательно содержит символы '@' и '.', а все остальные символы могут принимать значения: 'a-z', 'A-Z', '0-9' и '_'. Если email верен, то функция выводит "ДА", иначе "НЕТ".
#
# После объявления функции прочитайте (с помощью функции input) строку с email-адресом и вызовите функцию с этим аргументом.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.1.8
#
# Sample Input:
#
# sc_lib@list.ru
# Sample Output:
#
# ДА

# def check_email(e_mail):
#         flag = False
#         if '@' in e_mail and '.' in e_mail:
#                 for i in e_mail:
#                         if i == '@' or i == '.':
#                                 continue
#                         if 48 <= ord(i) <= 57 or 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or ord(i) == 95:
#                                 flag = True
#                         else:
#                                 flag = False
#                                 break
#         return flag
#
#
# # print(ord('a'), ord('z'), ord('A'), ord('Z'), ord('0'), ord('9'), ord('_'))
# e_mail_input= input()
# print('ДА' if check_email(e_mail_input) else 'НЕТ')


# Отличное решение через множества
# def check_mail(mail):
#     allow = set("abcdefghijklmnopqrstuvwxyz0123456789_@.")
#     nesessary = {"@", "."}
#     print("ДА") if nesessary <= mail <= allow else print("НЕТ")
#
#
# msg = set(input().lower())
# check_mail(msg)

from re import fullmatch


def is_email_correct(email: str) -> bool:
    reg = r'([a-zA-Z_0-9]+)'
    reg = fr'({reg}\.)*{reg}@({reg}\.)+{reg}'
    return fullmatch(reg, email)


print(('НЕТ', 'ДА')[bool(is_email_correct(input()))])
