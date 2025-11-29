def is_prime(num: int) -> bool:
    return num > 1 and all(num % d != 0 for d in range(2, int(num ** 0.5) + 1))


def sum_of_figures(num: int) -> int:
    return sum(int(x) for x in str(num))


l = tuple(int(input()) for _ in range(int(input())))
print(sum(sum_of_figures(x) for x in l if is_prime(x)))
