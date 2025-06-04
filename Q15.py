# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 17:45:49 2025

@author: saikr
"""

# Remove all duplicates from a list using a set, but return the final result as a list with the
# original order preserved.

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Example usage
original_list = [1, 2, 2, 3, 1, 4, 3, 5]
unique_list = remove_duplicates(original_list)

print("Original list:", original_list)
print("List after removing duplicates:", unique_list)