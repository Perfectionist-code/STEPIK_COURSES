from turtle import *

tracer(0)
screensize(5000, 5000)
r = 60
for _ in range(2):
    x, y = pos()
    goto(x + 6 * r, y + 2 * r)
    x, y = pos()
    goto(x + 0 * r, y - 2 * r)
for _ in range(3):
    x, y = pos()
    goto(x + 2 * r, y - 1 * r)
    x, y = pos()
    goto(x - 2 * r, y - 1 * r)
for _ in range(6):
    x, y = pos()
    goto(x - 2 * r, y + 1 * r)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, 'red')
update()
mainloop()
