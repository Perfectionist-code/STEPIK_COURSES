from turtle import *

screensize(5000,5000)
tracer(0)
r = 40
for _ in range(4):
    fd(3*r)
    lt(270)
    fd(5*r)
    rt(90)
lt(270)
for _ in range(3):
    fd(5*r)
    rt(90)
    fd(3*r)
    lt(270)

up()
for x in range(-50, 50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(5,'red')
update()
done()