# Подвиг 2. На вход программе подаются строки (URL-адреса, каждая с новой строки). В программе уже реализовано их чтение и сохранение в списке:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# Требуется заменить строках списка lst_in все пробелы на символ дефиса (-). Следует учесть, что может быть несколько подряд идущих пробелов. Полученные URL-адреса (строки) вывести на экран в столбик в порядке их следования в списке lst_in.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.6.2
#
# Sample Input:
#
# django chto  eto takoe    poryadok ustanovki
# model mtv   marshrutizaciya funkcii  predstavleniya
# marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya
# Sample Output:
#
# django-chto-eto-takoe-poryadok-ustanovki
# model-mtv-marshrutizaciya-funkcii-predstavleniya
# marshrutizaciya-obrabotka-isklyucheniy-zaprosov-perenapravleniya
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
for i in range(len(lst_in)):
    while '  ' in lst_in[i]:
        lst_in[i] = lst_in[i].replace('  ', ' ')
    lst_in[i] = lst_in[i].replace(' ', '-')
    print(lst_in[i])