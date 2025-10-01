from turtle import *

tracer(0)
screensize(5000, 5000)
r = 30
for _ in range(8):
    for _f in range(4):
        fd(5 * r)
        rt(30)
        fd(6 * r)
        rt(150)
    rt(60)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, 'red')

update()
mainloop()
