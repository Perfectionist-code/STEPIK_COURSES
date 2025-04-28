# Подвиг 2. Объявите класс Money так, чтобы объекты этого класса можно было создавать следующим образом:
#
# my_money = Money(100)
# your_money = Money(1000)
#
# Здесь при создании объектов указывается количество денег, которое должно сохраняться в локальном свойстве (атрибуте) money каждого экземпляра класса.
#
# P.S. На экран в программе ничего выводить не нужно.

# здесь объявляйте класс Money

from random import randint, choice

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.sp = (x1, y1)
        self.ep = (x2, y2)


class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.sp = (x1, y1)
        self.ep = (x2, y2)


class Ellipse:
    def __init__(self, x1, y1, x2, y2):
        self.sp = (x1, y1)
        self.ep = (x2, y2)



class_lst = (Line, Rect, Ellipse)
elements = [choice(class_lst)(randint(-100,100), randint(-100,100), randint(-100,100), randint(-100,100)) for _ in range(217)]

for element in elements:
    if isinstance(element, Line):
        element.sp = element.ep = (0,0)

for element in elements:
    print(type(element), element.__dict__)