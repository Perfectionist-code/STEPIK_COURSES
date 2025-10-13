from turtle import *

tracer(0)
screensize(5000, 5000)
r = 30
for k in range(2):
    fd(10 * r)
    rt(90)
    fd(20 * r)
    rt(90)
up()
fd(5 * r)
rt(90)
bk(10 * r)
lt(90)
down()
for k in range(2):
    fd(20 * r)
    rt(90)
    fd(40 * r)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, 'red')
update()
done()
