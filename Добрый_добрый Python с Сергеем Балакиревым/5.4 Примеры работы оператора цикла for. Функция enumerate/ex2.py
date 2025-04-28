# Подвиг 2. На вход программе подается строка с номером телефона. Ожидается следующий формат номера в строке:
#
# +7(xxx)xxx-xx-xx
#
# где x - это любая цифра. Число введенных символов считается верным (то есть, не может быть, чтобы отсутствовала какая-либо цифра или была лишняя). Необходимо прочитать строку из входного потока и проверить, что она содержит номер телефона в соответствии с приведенным форматом. Вывести "ДА", если это так и "НЕТ" в противном случае.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.4.2
#
# Sample Input:
#
# +7(123)456-78-99
# Sample Output:
#
# ДА

st = input()
sample = '+7(xxx)xxx-xx-xx'
for i, d in enumerate(st):
    if sample[i] != 'x':
        if sample[i] == d:
            continue
        else:
            print('НЕТ')
            break
    elif sample[i] == 'x' and d.isdigit():
            continue
    else:
        print('НЕТ')
        break
else:
    print('ДА')
