from turtle import *

tracer(0)
screensize(5000, 5000)
r = 60
for _ in range(3):
    x, y = pos()
    goto(x - 3 * r, y - 4 * r)
    x, y = pos()
    goto(x - 12 * r, y - 5 * r)
    x, y = pos()
    goto(x, y + 1 * r)
    x, y = pos()
    goto(x + 15 * r, y + 8 * r)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, 'red')
update()
mainloop()
