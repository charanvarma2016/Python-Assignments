# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 16:26:35 2025

@author: saikr
"""
"""15.Perfect Number Check
A number is perfect if it is equal to the sum of its proper divisors.
Write a function is_perfect(n) to check this.

Example: is_perfect(28) → True"""

def is_perfect(n):
    if n <= 0:
        return False

    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i

    return sum_of_divisors == n


print(is_perfect(28))  
print(is_perfect(12))
