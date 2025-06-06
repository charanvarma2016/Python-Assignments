# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 17:51:28 2025

@author: saikr
"""

"""6.Count Vowels in a String
Write a function count_vowels(s) that returns the number of vowels in a string.
Example: count_vowels(""charan") → 2"""
        
def count_vowels(s):
    vowels = "aeiouAEIOU"  
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("charan"))               