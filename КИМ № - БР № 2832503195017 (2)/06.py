from turtle import *

tracer(0)
screensize(5000, 5000)
r = 30
for _ in range(9):
    fd(22 * r)
    rt(90)
    fd(6 * r)
    rt(90)
up()
fd(1 * r)
rt(90)
fd(5 * r)
lt(90)
down()
for _ in range(9):
    fd(53 * r)
    rt(90)
    fd(75 * r)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(5, 'red')
update()
done()
