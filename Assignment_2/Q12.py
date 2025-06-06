# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 15:57:51 2025

@author: saikr
"""
"""12.Happy Number Check
A number is happy if repeatedly summing the squares of digits eventually reaches 1.
Write a function is_happy(n) to return True or False."""

def is_happy(n):
    seen = set()  # To keep track of numbers we've already seen

    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))  # Sum of squares of digits

    return n == 1

# Example usage
print(is_happy(19))  # Output: True (19 is a happy number)
print(is_happy(4))   # Output: False (4 is not a happy number)
