# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 17:40:47 2025

@author: saikr
"""
"""8. Operator Overloading
Implement a Vector2D class and overload +, -, *, and == operators for vector arithmetic."""

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    # Overloading the - operator
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    # Overloading the * operator (scalar multiplication)
    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    # Overloading the == operator
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # For pretty printing
    def __str__(self):
        return f"({self.x}, {self.y})"
    
v1 = Vector2D(2, 3)
v2 = Vector2D(4, 5)

print("v1:", v1)
print("v2:", v2)

# Addition
v3 = v1 + v2
print("v1 + v2 =", v3)

# Subtraction
v4 = v2 - v1
print("v2 - v1 =", v4)

# Scalar Multiplication
v5 = v1 * 3
print("v1 * 3 =", v5)

# Equality
print("v1 == v2?", v1 == v2)
v6 = Vector2D(2, 3)
print("v1 == v6?", v1 == v6)
