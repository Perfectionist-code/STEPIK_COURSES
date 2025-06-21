from abc import ABC, abstractmethod
from math import sqrt


class Shape(ABC):

    @abstractmethod
    def perimetr(self):
        ...

    @abstractmethod
    def area(self):
        ...


class TriangleError(Exception):
    def __str__(self):
        return 'Ошибка существования треугольника. Проверьте введённые стороны треугольника.'


class Triangle(Shape):
    @staticmethod
    def check_triangle(a, b, c):
        if not all([a + b > c, a + c > b, b + c > a]):
            raise TriangleError
        return True

    def perimetr(self, a, b, c):
        Triangle.check_triangle(a, b, c)
        return a + b + c

    def area(self, a, b, c):
        p = self.perimetr(a, b, c) / 2
        return sqrt(p * (p - a) * (p - b) * (p - c))

t = Triangle()
triangle = (int(input()), int(input()), int(input()))
print(t.perimetr(*triangle))
print(t.area(*triangle))
