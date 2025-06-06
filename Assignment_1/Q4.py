# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 17:20:22 2025

@author: saikr
"""

# Create a new list with the square of all even numbers from the list [1, 2, 3, 4, 5, 6] using
# list comprehension.

# Original list
numbers = [1, 2, 3, 4, 5, 6]

# List comprehension to get squares of even numbers
square_even = [x**2 for x in numbers if x % 2 == 0]

# Print the result
print("Squared even numbers:", square_even)