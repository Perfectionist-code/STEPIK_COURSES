from math import log2
# объявление функции
def determine_max_number_requests(num):
    return int(log2(num)) + 1

# считываем данные
n = int(input())

# вызываем функцию
print(determine_max_number_requests(n))