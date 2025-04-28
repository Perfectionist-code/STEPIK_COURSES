def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# объявление функции
def get_next_prime(num):
    while True:
        num += 1
        if is_prime(num):
            return num

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))