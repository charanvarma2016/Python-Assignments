# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 17:35:00 2025

@author: saikr
"""

# 11. Merge two dictionaries. If a key exists in both, keep the higher value.
# Example:
# d1 = {'a': 5, 'b': 8}, d2 = {'b': 10, 'c': 6}
# Result: {'a': 5, 'b': 10, 'c': 6}

def merge_dicts_max(d1, d2):
    # Start with a copy of the first dictionary
    merged = d1.copy()

    # Loop through the second dictionary
    for key, value in d2.items():
        if key in merged:
            # If key exists in both, keep the higher value
            merged[key] = max(merged[key], value)
        else:
            # If key is only in d2, add it
            merged[key] = value

    return merged

# Example
dict1 = {'a': 5, 'b': 8}
dict2 = {'b': 10, 'c': 6}

result = merge_dicts_max(dict1, dict2)

print("Merged dictionary:", result)