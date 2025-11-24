from turtle import *

tracer(0)
r = 30
screensize(5000, 5000)
for _ in range(5):
    fd(30 * r)
    rt(90)
    fd(40 * r)
    rt(90)
up()
fd(20 * r)
rt(90)
fd(5 * r)
rt(90)
down()
for _ in range(7):
    fd(10 * r)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(5, 'red')
update()
done()
