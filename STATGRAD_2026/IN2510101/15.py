def f(x,y):
    return (y>A) or (152 != 2*y+3*x) or (A <x)

for A in range(100,-1,-1):
    if all((f(x, y) for x in range(1, 10000) for y in range(1, 10000))):
        print(A)
        break
# ОТВЕТ: 30 2 часа 10 мин