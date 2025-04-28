# Подвиг 3. На вход программе подаются два натуральных числа a, b (a < b), записанные через пробел. Прочитайте их и выполните генерацию целочисленной случайной величины в диапазоне [a; b]. Выведите результат на экран.
#
# Ликбез: квадратная скобка - граница включается в диапазон; круглая скобка - граница исключается из диапазона.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/10/10.3.3
#
# Sample Input:
#
# -2 3
# Sample Output:
#
# -1

import random
random.seed(1)
a, b = input().split()
random_number = random.randint(int(a), int(b))
print(random_number)
