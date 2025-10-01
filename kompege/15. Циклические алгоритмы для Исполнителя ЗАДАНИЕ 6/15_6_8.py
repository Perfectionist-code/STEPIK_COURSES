from turtle import *

screensize(5000, 5000)
tracer(0)
up()
r = 30
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, 'red')
home()
down()
for _ in range(3):
    fd(7 * r)
    rt(90)
fd(8 * r)
for _ in range(3):
    lt(90)
    fd(5 * r)

update()
mainloop()
