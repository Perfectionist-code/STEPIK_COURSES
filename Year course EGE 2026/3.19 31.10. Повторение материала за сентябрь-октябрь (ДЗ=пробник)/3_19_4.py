from turtle import *

tracer(0)
screensize(5000, 5000)
r = 20
for _ in range(3):
    fd(r * 39)
    rt(90)
    fd(r * 48)
    rt(90)
up()
fd(r * 27)
rt(90)
fd(r * 24)
lt(90)
down()
for _ in range(3):
    fd(r * 29)
    rt(90)
    bk(r * 18)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(r * x, r * y)
        dot(5, 'red')
update()
done()
