#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 13:58:03 2025

@author: charan
"""
import numpy as np

# Step 1: Define the coefficient matrix A and the result vector b
A = np.array([
    [3, 2, -1],
    [2, -2, 4],
    [-1, 0.5, -1]
])

b = np.array([1, -2, 0])

# Step 2: Solve the system Ax = b
x = np.linalg.solve(A, b)

# Step 3: Print the solution
print("Solution [x, y, z]:", x)

# Step 4: Verify that Ax ≈ b
print("Verification (Ax):", np.dot(A, x))
print("Original b vector: ", b)
