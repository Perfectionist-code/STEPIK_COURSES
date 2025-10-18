from turtle import *

screensize(5000, 5000)
tracer(0)
r = 30
for _ in range(2):
    fd(13 * r)
    rt(90)
    fd(20 * r)
    rt(90)
up()
fd(8 * r)
rt(90)
bk(3 * r)
lt(90)
down()
for _ in range(2):
    fd(16 * r)
    rt(90)
    fd(8 * r)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, 'red')
update()
done()
