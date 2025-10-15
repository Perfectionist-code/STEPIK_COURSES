from turtle import *

screensize(5000, 5000)
tracer(0)
r = 30
for _ in range(2):
    fd(5 * r)
    rt(90)
    fd(8 * r)
    rt(90)
up()
fd(2 * r)
rt(90)
fd(3 * r)
lt(90)
down()
color('blue')
for _ in range(2):
    fd(4 * r)
    rt(90)
    fd(9 * r)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, 'red')
update()
done()
