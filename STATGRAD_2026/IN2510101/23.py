def f(curr, end, not_num):
    if curr > end or curr == not_num: return 0
    if curr == end: return 1
    return f(curr + 1, end, not_num) + f(curr * 2, end, not_num) + f(curr * 3, end, not_num)

print(f(6, 14, 18)*f(14, 48,18) + f(6, 18, 14)*f(18, 48,14))

# Ответ: 45 3 часа 25 мин
