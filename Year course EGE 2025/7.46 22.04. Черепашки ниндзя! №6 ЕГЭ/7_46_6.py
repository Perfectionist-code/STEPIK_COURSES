from turtle import tracer, up, update, color, down, fd, bk, rt, lt, dot, screensize, width, done, goto

tracer(0)
screensize(5000, 5000)
width(5)
color('black')
r = 30
for _ in range(2):
    fd(21 * r)
    rt(90)
    fd(27 * r)
    rt(90)
up()
fd(9 * r)
rt(90)
fd(10 * r)
lt(90)
down()
color('blue')
for _ in range(2):
    fd(86 * r)
    rt(90)
    fd(47 * r)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(5, 'red')
up()
update()
done()
