def get_r(n: int):
    r = f'{num:b}'
    cnt_1 = r[1::2].count('1')
    cnt_0 = r[::2].count('0')
    # print(r, cnt_1,cnt_0)
    return abs(cnt_1-cnt_0)


for num in range(1, 10000):
    if (d := get_r(num)) == 5:
        print(num)
        break

