from turtle import *

tracer(0)
screensize(5000, 5000)
r = 60
for _ in range(5):
    x, y = pos()
    goto(x + 6 * r, y + 8 * r)
    x, y = pos()
    goto(x - 8 * r, y + 4 * r)
    x, y = pos()
    goto(x + 2 * r, y - 12 * r)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, 'red')
update()
mainloop()
