for num in range(1, 1000):
    for _ in range(2):
        num = bin(num)[2:]
        s_n = sum(map(int, num))
        num = num + str(s_n % 2)
        num = int(num, 2)
    print(num)
    if num > 80:
        break
