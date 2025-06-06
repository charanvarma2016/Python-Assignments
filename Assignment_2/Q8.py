# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 15:26:32 2025

@author: saikr
"""
"""8.Armstrong Number Check
Write a function is_armstrong(n) that checks if n is an Armstrong number.
Example: is_armstrong(153) → True"""

def is_armstrong(n):
    digits = str(n)                     # Convert number to string to access digits
    power = len(digits)                # Number of digits
    total = sum(int(digit) ** power for digit in digits)  # Sum of each digit raised to the power
    return total == n                  # Check if the sum equals the original number


print(is_armstrong(1634))
