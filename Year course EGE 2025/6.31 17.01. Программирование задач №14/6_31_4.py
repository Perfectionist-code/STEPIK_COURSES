num = 2 * 729 ** 2014 + 2 * 243 ** 2016 - 2 * 81 ** 2018 + 2 * 27 ** 2020 - 2 * 9 ** 2022 - 2024
cnt = 0
while num:
    num, r = divmod(num, 27)
    if r > 9:
        cnt += 1
print(cnt)
