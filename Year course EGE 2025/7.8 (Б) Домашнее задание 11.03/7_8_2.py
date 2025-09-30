def f(x,y):
    return (x+y<=30) or (y<=x+2) or (y>=A)

for A in range(100, 0,-1):
    if all(f(x,y) for x in range(10000) for y in range(10000)):
        print(A)
        break
