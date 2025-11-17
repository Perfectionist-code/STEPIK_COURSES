from turtle import *

tracer(0)
screensize(5000, 50000)
r = 30
for _ in range(2):
    fd(9 * r)
    rt(90)
    fd(15 * r)
    rt(90)
up()
fd(12 * r)
rt(90)
down()
for _ in range(2):
    fd(6 * r)
    rt(90)
    fd(12 * r)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(5,'red')
update()
done()
