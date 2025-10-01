from turtle import *

tracer(0)
screensize(5000, 5000)
r = 60
for _ in range(5):
    x, y = pos()
    goto(x + 5 * r, y + 4 * r)
    x, y = pos()
    goto(x + 4 * r, y - 4 * r)
    x, y = pos()
    goto(x - 7 * r, y - 2 * r)
    x, y = pos()
    goto(x - 2 * r, y + 2 * r)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, 'red')
update()
mainloop()
