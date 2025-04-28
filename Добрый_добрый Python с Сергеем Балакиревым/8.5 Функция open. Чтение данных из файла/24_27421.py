# Тип 24 _27686 Текстовый файл состоит не более чем из 106 символов X, Y и Z. Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
#
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

# Вариант решения задачи через удаление ненужных символов и поиска элемента списка максимальной длины.
# file = open('24_27421.txt', mode = 'r')
# file_cut_lst = file.read().replace('Y',' ').replace('Z',' ').split()
# s = sorted({x for x in file_cut_lst})
# print(len(max(s, key = len)))
# file.close()


# Решение через последовательный перебор элементов
file = open('24_27421.txt', mode = 'r')
# string_from_file = file.read()
# print(sys.getsizeof(string_from_file))
length_lst = []
count_max = 0
count_char_X = 0
for char in file.read():
    if char != 'X':
        count_char_X = 0
    elif char == 'X':
        count_char_X += 1
        if count_max < count_char_X:
            count_max = count_char_X

print(count_max)
file.close()
