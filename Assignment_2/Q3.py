# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 16:55:56 2025

@author: saikr
"""

"""3.Factorial (Loop + Function)
Create a function factorial(n) using a loop (not recursion).
Example: factorial(5) → 120"""

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print("factorial(7)", factorial(7)) 