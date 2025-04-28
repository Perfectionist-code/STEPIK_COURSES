# Программа поиска всех простых чисел в диапазоне от n до m (код GPT Chat)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num*0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(n, m):
    primes = []
    for num in range(n, m + 1):
        if is_prime(num):
            primes.append(num)
    return primes

n = int(input("Введите n: "))
m = int(input("Введите m: "))
print(find_primes(n, m))