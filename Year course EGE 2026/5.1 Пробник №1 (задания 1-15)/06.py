from turtle import *

tracer(0)
screensize(5000, 5000)
r = 30
for _ in range(5):
    fd(35 * r)
    rt(90)
    fd(24 * r)
    rt(90)
up()
rt(90)
fd(7 * r)
rt(90)
fd(5 * r)
down()
for _ in range(1001):
    rt(90)
    fd(20 * r)
    rt(90)
    fd(36 * r)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(5, 'red')
update()
done()
