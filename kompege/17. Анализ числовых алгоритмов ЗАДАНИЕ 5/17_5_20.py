def get_r(n: int):
    n = str(n)
    sum_even = sum([int(x) for x in n if int(x) % 2 == 0])
    sum_even_position = sum([int(x) for i, x in enumerate(n, 1) if i % 2 == 0])
    return abs(sum_even - sum_even_position)


for num in range(2, 1000):
    if get_r(num) == 9:
        print(num)
        break
