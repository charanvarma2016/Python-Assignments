# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 17:23:18 2025

@author: saikr
"""

# Write a function that takes a list of tuples and returns the tuple with the maximum sum.

def max_sum_tuple(tuples_list):
    # Start with the first tuple as the max
    max_tuple = tuples_list[0]
    max_sum = sum(max_tuple)

    # Loop through the rest of the tuples
    for t in tuples_list[1:]:
        current_sum = sum(t)
        if current_sum > max_sum:
            max_sum = current_sum
            max_tuple = t

    return max_tuple

# Example usage
tuples = [(5, 1), (9, 6), (2, 3), (4, 4)]
result = max_sum_tuple(tuples)

print("Tuple with maximum sum:", result)