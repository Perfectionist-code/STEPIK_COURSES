from turtle import *

screensize(5000, 5000)
tracer(0)
r = 20

fd(9 * r)
rt(90)
for _ in range(2):
    fd(3 * r)
    rt(90)
    fd(3 * r)
    rt(270)
for _ in range(2):
    fd(3 * r)
    rt(90)
fd(9 * r)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, 'red')

update()
mainloop()
