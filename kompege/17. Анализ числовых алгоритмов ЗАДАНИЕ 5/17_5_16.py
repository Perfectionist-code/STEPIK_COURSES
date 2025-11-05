def get_r(n: int):
    a, b, c = [int(x) for x in str(n)]
    r = sorted((a ** 2 + b ** 2, b ** 2 + c ** 2), reverse=True)
    r = str(r[0]) + str(r[1])
    return int(r)


for num in range(100, 1000):
    if get_r(num) == 9010:
        print(num)
        break
