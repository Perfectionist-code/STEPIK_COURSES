# Подвиг 4. На вход программе подается строка с названиями городов, записанных через пробел. Необходимо прочитать эту строку и сформировать список с помощью list comprehension, содержащий названия городов длиной более пяти символов. Элементы полученного списка вывести в одну строчку через пробел.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.8.4
#
# Sample Input:
#
# Казань Уфа Москва Челябинск Омск Тур Самара
# Sample Output:
#
# Казань Москва Челябинск Самара

lst = [x for x in input().split() if len(x) > 5]
print(*lst)

# n = int(input())
# mtx = [[int(i == j) for j in range(n)] for i in range(n)]
# for row in mtx:
#     print(*row)