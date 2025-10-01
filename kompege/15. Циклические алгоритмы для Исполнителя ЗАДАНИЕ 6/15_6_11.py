from turtle import *

tracer(0)
screensize(5000, 5000)
r = 20
for i in range(2):
    fd(24 * r)
    rt(90)
    fd(10 * r)
    rt(90)
fd(3 * r)
lt(90)
fd(13 * r)
rt(90)
for _ in range(2):
    fd(9 * r)
    rt(90)
    fd(32 * r)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, 'red')
update()
mainloop()
