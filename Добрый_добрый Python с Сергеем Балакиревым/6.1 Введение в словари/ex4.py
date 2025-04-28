# Подвиг 6. На вход программе подаются данные в формате ключ=значение, записанные через пробел. Необходимо прочитать строку с этими данными и на их основе сформировать словарь d. Затем удалить из этого словаря ключи 'False' и '3', если они существуют. Ключами и значениями словаря являются строки. Вывести полученный словарь на экран командой:
#
# print(*sorted(d.items()))
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/6/6.1.6
#
# Sample Input:
#
# лена=имя дон=река москва=город False=ложь 3=удовлетворительно True=истина
# Sample Output:
#
# ('True', 'истина') ('дон', 'река') ('лена', 'имя') ('москва', 'город')

lst_in = [item.split(sep = '=') for item in input().split()]
d = {key: value for key , value in lst_in}
del_item = ['False', '3']
for d_i in del_item:
    if d_i in d:
        del d[d_i]
print(*sorted(d.items()))

# я провел тест самых популярных решений на 1 млн значений. Публикую результаты от самых быстрых до самых медленных. Хотя в целом результаты похожи.
# n=[f'{i}={i+1}' for i in range(1000000)]
#
# d = dict(pair.split('=') for pair in n)
# for key in ('False', '3'):
#     d.pop(key, 'Да не очень то и надо')
# 1.6280407905578613
#
# d = {i.split('=')[0]: i.split('=')[1] for i in n if i.split('=')[0] not in {'False', '3'}}
# 2.9005956649780273
#
# d = dict([i.split('=') for i in n])
# del_values = [ 'False', '3']
# for i in del_values:
#     if i in d:
#         del d[i]
# 4.367959499359131
#
# d = dict([[k,v] for el in n for k,v in [el.split('=')] if k not in {'False','3'}])
# 4.674291610717773
#
# d = dict([i.split('=') for i in n if i.split('=')[0] not in {'False','3'}])
# 5.206029891967773