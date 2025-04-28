# Подвиг 7. На вход программы подаются целые числа, записанные в одну строку через пробел (не менее четырех). Необходимо прочитать эти числа и среди них найти три наименьших числа. Выведите на экран найденные три числа в порядке возрастания в одну строчку через пробел. Программу реализовать без использования условного оператора.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/3/3.8.7
#
# Sample Input:
#
# 8 11 -5 10 -1 0 7
# Sample Output:
#
# -5 -1 0

lst = list(map(int, input().split()))
lst_ = [lst.pop(lst.index(min(lst))), lst.pop(lst.index(min(lst))), lst.pop(lst.index(min(lst)))]
lst_.sort()
print(*lst_)
