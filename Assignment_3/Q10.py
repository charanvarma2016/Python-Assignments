# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 17:54:07 2025

@author: saikr
"""
"""10. Abstract Base Classes
Use the abc module to create an abstract class Shape with an abstract method area().
Implement concrete classes Rectangle, Circle, and Triangle."""

from abc import ABC, abstractmethod
import math

# Abstract Base Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


# Rectangle subclass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Triangle subclass
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Example usage
shapes = [
    Rectangle(4, 5),
    Circle(3),
    Triangle(6, 2)
]

for shape in shapes:
    print(f"{shape.__class__.__name__} Area: {shape.area():.2f}")
