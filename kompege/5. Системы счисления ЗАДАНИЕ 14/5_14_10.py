def num_to_cs(num, cs):
    res = []
    while num:
        num, r = divmod(num, cs)
        res.append(str(r))
    return ''.join(res[::-1])


num = 5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875
num = num_to_cs(num, 6)
print(num.count('5') - num.count('0'))