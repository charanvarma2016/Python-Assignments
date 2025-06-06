# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 17:40:54 2025

@author: saikr
"""

# Invert a dictionary

original = {'a': 1, 'b': 2, 'c': 1}

inverted = {}
for key, value in original.items():
    inverted.setdefault(value, []).append(key)

print("Inverted with duplicates grouped:", inverted)