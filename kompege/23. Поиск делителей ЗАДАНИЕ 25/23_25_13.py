def is_prime(num:int) -> bool:
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            return False
    return True

for n in range(6080068, 6080177):
    if is_prime(n):
        print(n)