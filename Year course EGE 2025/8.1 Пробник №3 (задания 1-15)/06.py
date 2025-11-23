from turtle import *

tracer(0)
screensize(5000, 5000)
r = 30
for _ in range(7):
    rt(90)
    fd(7 * r)
    rt(90)
    fd(6 * r)
up()
rt(90)
fd(3 * r)
rt(90)
fd(1 * r)
down()
for _ in range(4):
    rt(90)
    fd(6 * r)
    rt(90)
    fd(11 * r)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(5, 'red')
update()
done()
