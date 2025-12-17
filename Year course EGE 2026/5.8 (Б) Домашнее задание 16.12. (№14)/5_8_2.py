num = 3 * 2187 ** 2020 + 3 * 729 ** 2021 - 2 * 81 ** 2022 + 27 ** 2023 - 4 * 3 ** 2024 - 2029
cnt = 0
while num:
    num, r = divmod(num, 27)
    if r > 9:
        cnt += 1
print(cnt)
