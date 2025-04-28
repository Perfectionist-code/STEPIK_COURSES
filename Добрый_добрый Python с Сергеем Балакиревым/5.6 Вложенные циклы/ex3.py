# Подвиг 3. На вход программе подается натуральное число n. Необходимо его прочитать и найти все простые числа (нацело делятся только на 1 и на себя), которые меньше числа n, то есть, в диапазоне [2; n). Результат вывести на экран в строчку через пробел.
#
# Ликбез: квадратная скобка - граница включается; круглая скобка - граница исключается. Например [2; n) - диапазон от 2 до n-1 целых чисел.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.6.3
#
# Sample Input:
#
# 11
# Sample Output:
#
# 2 3 5 7

n = int(input())
n = abs(n)
prime_numbers = []
for num in range(2, n):
    _bool = True
    if n < 2:
        _bool = False
    else:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                _bool = False
        if _bool:
            prime_numbers.append(num)
print(*prime_numbers)