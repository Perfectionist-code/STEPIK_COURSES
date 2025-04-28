# Подвиг 3. На автомойку в течение квартала заезжали машины. Их гос. номера фиксировались в журнале, следующим образом (пример):
#
# Е220СК
# А120МВ
# В101АА
# Е220СК
# А120МВ
#
# В программе уже реализовано чтение этих строк и сохранение в списке:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# На основе этого списка через генератор множеств сформировать еще один список уникальных машин. На экран вывести число уникальных машин.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/6/6.6.3
#
# Sample Input:
#
# А323ГД
# Д456ВВ
# Б001ББ
# Д456ВВ
# С111СС
# Sample Output:
#
# 4

import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_unic = list({value for value in lst_in})
print(len(lst_unic))