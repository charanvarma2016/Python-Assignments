# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 13:11:56 2025

@author: saikr
"""

"""" 1.Sum of Digits
Write a function sum_of_digits(n) that returns the sum of the digits of a number n.
Example: sum_of_digits(1234) → 10 """


def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total
        
print (sum_of_digits(1234))




