# Подвиг 3. На вход программе подаются целые числа, записанные через пробел. Необходимо их прочитать и сохранить в виде списка (или кортежа). Затем, объявить рекурсивную функцию с именем get_rec_sum для вычисления суммы прочитанных чисел. То есть, функция get_rec_sum в итоге должна возвращать значение суммы. (Выводить на экран она ничего не должна). Первым параметром в функцию следует передавать список чисел. Остальные параметры продумайте самостоятельно.
#
# Вызовите функцию get_rec_sum и выведите на экран значение суммы, которое она вернула.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.7.3
#
# Sample Input:
#
# 8 11 -5 4 3
# Sample Output:
#
# 21

def get_rec_sum(F,sum=0) :
    if not F :
        return sum
    else :
        sum += F.pop()
        return get_rec_sum(F,sum)


N = [int(x) for x in input().split()]
print(get_rec_sum(N.copy()))
print(N)

# lst1 = [int(i) for i in input().split()]
#
# def get_rec_sum(lst):
#     head, *tail = lst
#     return head + get_rec_sum(tail) if tail else head
#
# print(get_rec_sum(lst1))
