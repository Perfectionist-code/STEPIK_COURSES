from turtle import *

screensize(5000, 5000)
tracer(0)
r = 30
for _ in range(5):
    fd(15 * r)
    lt(90)
    fd(25 * r)
    lt(90)
up()
fd(4 * r)
lt(90)
fd(12 * r)
lt(90)
down()
for _ in range(6):
    fd(38 * r)
    rt(90)
    fd(22 * r)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, 'red')
update()
mainloop()
