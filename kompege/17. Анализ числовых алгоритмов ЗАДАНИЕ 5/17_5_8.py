def get_r(n: int):
    r = f'{2 * n:b}'
    for _ in range(2):
        r += str(sum(int(x) for x in r) % 2)
    return int(r, 2)


for num in range(1, 1000):
    if get_r(num) > 1017:
        print(num)
        break
