from string import printable


def is_prime(num: int) -> bool:
    return num > 1 and all(num % d != 0 for d in range(2, int(num ** .5) + 1))


cnt = 0
for x in printable[:18]:
    if is_prime(int(f'56{x}3', 18) + int(f'4{x}9', 18) - int(f'57{x}1', 18)):
        cnt += 1
print(cnt)
