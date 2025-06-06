# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 17:55:38 2025

@author: saikr
"""
"""7.Sum of Even Numbers in Range
Write a function sum_even(start, end) that returns the sum of even numbers between start and
end (inclusive).
Example: sum_even(1, 10) → 30"""


def sum_even(start, end):
    total = 0
    for num in range(start, end + 1):  # Include 'end' in the range
        if num % 2 == 0:  # Check if the number is even
            total += num
    return total


print(sum_even(1, 10)) 