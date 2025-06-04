# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 17:32:34 2025

@author: saikr
"""

# Write a program that takes a string and returns a dictionary with each character's
# frequency count.

def char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1  # Increment count if character already seen
        else:
            freq[char] = 1   # Initialize count if seeing for the first time
    return freq

# Example usage
input_string = "charan"
result = char_frequency(input_string)

print("Character frequency:", result)
