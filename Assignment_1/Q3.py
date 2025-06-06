# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 17:18:50 2025

@author: saikr
"""

# Write a program to remove duplicates from a list without using set(), while keeping the
# original order.

# Original list with duplicates
original_list = [10, 20, 30, 30, 40, 40, 50]

# List to store unique elements
unique_list = []

# Loop through original list and add only unique elements
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

# Print the result
print("List after removing duplicates:", unique_list)