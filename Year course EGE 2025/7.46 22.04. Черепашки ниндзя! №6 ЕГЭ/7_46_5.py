from turtle import *

screensize(5000, 5000)
tracer(0)
r = 30
for _ in range(4):
    fd(10 * r)
    rt(90)
up()
rt(90)
fd(5 * r)
lt(90)
down()
color('blue')
for _ in range(4):
    fd(10 * r)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(6, 'red')
update()
done()
