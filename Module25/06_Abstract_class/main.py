from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14


class Rectangle(Shape):
    def __init__(self, hight, withg):
        self.hight = hight
        self.withg = withg

    def area(self):
        return self.hight * self.withg


class Triangle(Shape):
    def __init__(self, katet_a, katet_b):
        self.katet_a = katet_a
        self.katet_b = katet_b

    def area(self):
        return self.katet_a * self.katet_b / 2


# Примеры работы с классом:
# Создание экземпляров классов
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)


# Вычисление площади фигур
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()

# Вывод результатов
print("Площадь круга:", circle_area)
print("Площадь прямоугольника:", rectangle_area)
print("Площадь треугольника:", triangle_area)
