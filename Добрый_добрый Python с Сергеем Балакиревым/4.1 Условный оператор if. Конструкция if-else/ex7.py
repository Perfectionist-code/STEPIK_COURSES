# ППодвиг 7. На вход программе подается строка из названий городов, записанных через пробел. Необходимо прочитать эту строку и сформировать на ее основе список cities из названий городов. Затем, проверить, если в списке cities присутствует город Москва, то удалить этот элемент из списка. Вывести на экран результирующий список cities командой:
#
# print(*cities)
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/4/4.1.7
#
# Sample Input:
#
# Уфа Астрахань Москва Самара Казань
# Sample Output:
#
# Уфа Астрахань Самара Казань

cities = list(input().split())
triger = 'Москва'
if triger in cities:
    cities.pop(cities.index(triger))
print(*cities)