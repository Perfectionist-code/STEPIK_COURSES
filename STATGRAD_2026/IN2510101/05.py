for n in range(500):
    R = f'{n:b}'
    if n % 5 == 0:
        R += '11'
    else:
        R += f'{(n // 5):b}'
    R = int(R, 2)
    print(R, n)
    if R >= 783 and n % 2:
        print('---' * 5)
        print(n)
        break

# ОТВЕТ: 49
