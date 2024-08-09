 ### 1.Create a base class called shape with a method area.
 # create subclasses Circle, Square and Triangle that implement the area method.
 # Demonstrate polymorphism by creating a list of different shape objects
 # and iterating through it to calculate their areas

import math

class Shape:
    def area(self):
        return 0

class Circle(Shape):
     def __init__(self,radius):
         self.radius=radius

     def area(self):
         return math.pi * (self.radius ** 2)


class Square(Shape):
    def __init__(self, side):
         self.side= side

    def area(self):
         return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
         self.base= base
         self.height = height

    def area(self):
         return 0.5* self.base * self.height

side = float(input("Enter the side length of the square: "))
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
radius = float(input("Enter the radius of the circle: "))

square = Square(side)
triangle = Triangle(base, height)
circle = Circle(radius)

print(f"Square area: {square.area()}")
print(f"Triangle area: {triangle.area()}")
print(f"Circle area: {circle.area()}")


### 2. Create a class called Rectangle with private attribute for width and height.
# provide getter and setter methods to access and modify these attribute.
# include a method to calculte the area of the rectangle.

class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def width(self):
        return self._width

    def width(self,value):
        if value >0:
            self._width=value
        else:
            print("width must be positive")

    def height(self):
        return self._height

    def height(self,value):
        if value > 0:
            self._height=value
        else:
            print("height must be positive")

    def area(self):
        return self.width * self.height

width= int(input("Enter the width of the rectangle:"))
height=int(input("Enter the height of the rectangle:"))

rect=Rectangle(width,height)

print("Width:", rect.width)
print("Height:", rect.height)
print("Area:", rect.area())