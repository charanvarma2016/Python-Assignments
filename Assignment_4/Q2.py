#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 13:27:05 2025

@author: charan
"""

import numpy as np

# Original array
arr = np.arange(1, 31)

# Reshape into a 5x6 matrix
matrix = arr.reshape(5, 6)

# Sum of each row
row_sums = np.sum(matrix, axis=1)

# Mean of each column
column_means = np.mean(matrix, axis=0)

# Outputs
print("Reshaped matrix (5x6):\n", matrix)
print("Sum of each row:\n", row_sums)
print("Mean of each column:\n", column_means)