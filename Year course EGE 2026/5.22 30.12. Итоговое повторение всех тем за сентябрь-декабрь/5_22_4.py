from turtle import *

tracer(0)
screensize(5000, 5000)
r = 20
for _ in range(6):
    fd(33 * r)
    rt(90)
    fd(20 * r)
    rt(90)
up()
fd(3 * r)
rt(90)
fd(9 * r)
lt(90)
down()
for _ in range(6):
    fd(24 * r)
    rt(90)
    fd(25 * r)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(5, 'red')
update()
done()
