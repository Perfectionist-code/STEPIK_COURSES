from turtle import *

screensize(5000, 5000)
r = 30
tracer(0)
for _ in range(7):
    fd(15 * r)
    rt(90)
    fd(23 * r)
    rt(90)
up()
fd(3 * r)
rt(90)
fd(5 * r)
lt(90)
down()
for _ in range(7):
    fd(252 * r)
    rt(90)
    fd(398 * r)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(5, 'red')
update()
done()

# ОТВЕТ: 101084  (253*399 + 5*16+ 3*19)
