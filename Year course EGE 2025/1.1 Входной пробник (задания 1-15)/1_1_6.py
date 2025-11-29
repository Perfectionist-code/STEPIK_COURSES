from idlelib.rpc import request_queue
from turtle import *

tracer(0)
screensize(5000, 5000)
r = 30
for _ in range(2):
    fd(15 * r)
    lt(90)
    fd(20 * r)
    lt(90)
up()
rt(90)
bk(7 * r)
lt(90)
fd(9 * r)
down()
for _ in range(2):
    fd(17 * r)
    rt(90)
    fd(15 * r)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(5, 'red')
update()
done()
