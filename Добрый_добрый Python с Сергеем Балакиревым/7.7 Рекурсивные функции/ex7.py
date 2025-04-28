# Великий подвиг 8. На вход программе подаются целые числа, записанные через пробел. Необходимо их прочитать и сохранить в списке. Затем, выполнить сортировку этого списка по возрастанию с помощью алгоритма сортировки слиянием. Функция должна возвращать новый отсортированный список.
#
# Вызовите результирующую функцию сортировки для введенного списка и отобразите результат на экран в виде последовательности чисел, записанных через пробел.
#
# Подсказка: для разбиения списка и его последующей сборки используйте рекурсивные функции.
#
# P. S. Теория сортировки в видео предыдущего шага.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.7.8
#
# Sample Input:
#
# 8 11 -6 3 0 1 1
# Sample Output:
#
# -6 0 1 1 3 8 11


def merge_sort(arr) :
    if len(arr) <= 1 :
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid :])

    return merge(left_half,right_half)


def merge(left,right) :
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            sorted_list.append(left[i])
            i += 1
        else :
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i :])
    sorted_list.extend(right[j :])

    return sorted_list


# Ввод данных
input_numbers = input("Введите целые числа, разделенные пробелами: ")
numbers = list(map(int,input_numbers.split()))

# Сортировка и вывод
sorted_numbers = merge_sort(numbers)
print(' '.join(map(str,sorted_numbers)))