import turtle
def regular_hexagon(length, star_angle = 60, count = 5, step_angle = 45):
    turtle.speed(100)
    for i in range(count):
        turtle.forward(length)
        turtle.left(star_angle)
    turtle.home()
    pass


l = int(input('Введите размер стороны шестиугольника в пикселях: '))
regular_hexagon(l)
turtle.mainloop()
