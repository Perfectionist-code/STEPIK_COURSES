# Подвиг 5. На вход программе подаются данные в формате ключ=значение, записанные через пробел. Необходимо прочитать строку с этими данными и на их основе сформировать словарь. Затем проверить, существуют ли в словаре ключи со значениями: 'house', 'True' и '5' (все ключи - строки). Если все они существуют, то вывести на экран "ДА", иначе "НЕТ".
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/6/6.1.5
#
# Sample Input:
#
# вологда=город house=дом True=1 5=отлично 9=божественно
# Sample Output:
#
# ДА

lst_in = [item.split(sep = '=') for item in input().split()]
d = {key: value for key , value in lst_in}
print(d)
if  'house' in d and 'True' in d and '5' in d:
    print('ДА')
else:
    print('НЕТ')


# d = dict([i.split('=') for i in input().split()])
# print('ДА' if 'house' in d and 'True' in d and '5' in d else 'НЕТ')

# print('ДА' if all(i in d for i in ('house', 'True', '5')) else "НЕТ")