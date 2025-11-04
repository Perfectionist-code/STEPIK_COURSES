from math import prod
def get_r(n: int):
    n = str(n)
    res = sorted((prod(map(int, n[:2])), prod(map(int, n[2:]))))
    return int(str(res[0]) + str(res[1]))


for num in range(9999, 999, -1):
    if (d := get_r(num)) == 1214:
        print(num)
        break


