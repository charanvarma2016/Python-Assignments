#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 13:49:15 2025

@author: charan
"""
import numpy as np

# Step 1: Create a 5x5 matrix with random integers from 1 to 10
matrix = np.random.randint(1, 11, size=(5, 5))
print("Original 5x5 matrix:\n", matrix)

# Step 2: Create 1D array
arr = np.array([1, 2, 3, 4, 5])
print("\n1D array:\n", arr)

# Step 3: Add the array to each column (broadcast row vector down each column)
matrix = matrix + arr[:, np.newaxis]
print("\nAfter adding array to each column:\n", matrix)

# Step 4: Multiply each row by the array
matrix = matrix * arr[:, np.newaxis]
print("\nAfter multiplying each row by the array:\n", matrix)
