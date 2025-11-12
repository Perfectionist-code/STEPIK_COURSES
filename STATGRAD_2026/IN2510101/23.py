def f(curr, end, cnt):
    if curr == 14 or curr == 18: cnt += 1
    if curr > end: return 0
    if curr == end: return cnt > 0
    return f(curr + 1, end, cnt) + f(curr * 2, end, cnt) + f(curr * 3, end, cnt)


print(f(6, 48, 0))

# Ответ: 69 3 часа 25 мин ВЕРНО!
