import turtle
def square(length, star_angle = 20, count = 1):
    turtle.speed(250)
    for i in range(1, count + 1):
        turtle.left(star_angle * i)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.home()
    pass


l = int(input('Введите размер квадрата в пикселях: '))
a = int(input('Введите начальный угол поворота в градусах: '))
c = int(input('Введите количество квадратов, для черепашки: '))
square(l, a, c)
turtle.mainloop()
