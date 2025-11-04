def f(n):
    # print('*')
    global s
    s += 1
    if n >= 1:
        # print('*')
        s += 1
        f(n - 1)
        f(n - 3)
        # print('*')
        s += 1


s = 0
f(40)
print(s)
