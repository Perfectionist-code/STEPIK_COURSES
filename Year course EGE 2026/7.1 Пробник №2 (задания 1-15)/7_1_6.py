from turtle import *

tracer(0)
screensize(5000, 5000)
r = 30
for _ in range(4):
    fd(9 * r)
    lt(180)
    bk(10 * r)
    rt(90)
up()
bk(7 * r)
lt(90)
fd(3 * r)
rt(90)
down()
for _ in range(2):
    fd(17 * r)
    lt(90)
    fd(20 * r)
    lt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(5, 'red')
update()
done()
