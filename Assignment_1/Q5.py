# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 17:21:54 2025

@author: saikr
"""

# Given a list of integers, split it into two lists: one with even numbers and one with odd
# numbers.


# Original list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Initialize two empty lists
even_numbers = []
odd_numbers = []

# Loop through the original list
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# Print the results
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)