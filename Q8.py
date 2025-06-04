# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 17:30:47 2025

@author: saikr
"""

# Convert a nested list to a tuple:
# Example Input: [[1, 2], [3, 4], [5, 6]]
# Expected Output: ((1, 2), (3, 4), (5, 6))

# Input nested list
nested_list = [[1, 2], [3, 4], [5, 6]]

# Convert each inner list to a tuple and wrap the result in a tuple
nested_tuple = tuple(tuple(inner) for inner in nested_list)

# Print the result
print("Converted tuple:", nested_tuple)