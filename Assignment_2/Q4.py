# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 17:16:57 2025

@author: saikr
"""

"""4.Reverse a Number
Write a function reverse_number(n) that reverses the digits of a number.
Example: reverse_number(123) → 321"""



def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10            # Get the last digit
        reversed_num = reversed_num * 10 + digit  # Add digit to reversed_num
        n = n // 10               # Remove the last digit from n
    return reversed_num

# Example usage
print(reverse_number(12345))