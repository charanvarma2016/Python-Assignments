#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 13:25:17 2025

@author: saiprasanth
"""

import numpy as np

# Step 1: Create a 6x6 matrix with random integers between 10 and 50
matrix = np.random.randint(10, 51, size=(6, 6))
print("Original Matrix:\n", matrix)

# Step 2: Set the diagonal elements to 0
np.fill_diagonal(matrix, 0)
print("\nAfter setting diagonal to 0:\n", matrix)

# Step 3: Replace elements above the diagonal with 99
rows, cols = matrix.shape
for i in range(rows):
    for j in range(i + 1, cols):
        matrix[i, j] = 99
print("\nAfter setting elements above diagonal to 99:\n", matrix)

# Step 4: Extract the bottom-right 3x3 submatrix
submatrix = matrix[-3:, -3:]
print("\nBottom-right 3x3 submatrix:\n", submatrix)