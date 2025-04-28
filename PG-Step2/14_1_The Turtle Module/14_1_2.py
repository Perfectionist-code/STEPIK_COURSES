import turtle
def square(length, star_angle = 0, count = 8, step_angle = 45):
    turtle.speed(100)
    for i in range(count):
        turtle.left(star_angle + i * step_angle)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.home()
    pass


l = int(input('Введите размер квадрата в пикселях: '))
square(l)
turtle.mainloop()
