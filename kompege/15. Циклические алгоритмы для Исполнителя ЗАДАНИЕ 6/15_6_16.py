from turtle import *

tracer(0)
screensize(5000, 5000)
r = 60
for _ in range(10):
    x, y = pos()
    goto(x + 3 * r, y + 6 * r)
    x, y = pos()
    goto(x + 7 * r, y - 2 * r)
    x, y = pos()
    goto(x - 10 * r, y - 4 * r)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, 'red')
update()
mainloop()
