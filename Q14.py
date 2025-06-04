# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 17:44:02 2025

@author: saikr
"""

# Take two sets, print:
# a) Elements common to both
# b) Elements only in one of the sets

# Define the sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# a) Elements common to both (intersection)
common_elements = set1 & set2  

# b) Elements only in one of the sets (symmetric difference)
unique_elements = set1 ^ set2  

# Print the results
print("a) Common elements:", common_elements)
print("b) Elements only in one set:", unique_elements)