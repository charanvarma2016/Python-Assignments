#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 13:52:33 2025

@author: charan
"""
import numpy as np

# Step 1: Generate a symmetric 4x4 matrix with integers from 1 to 9
A = np.random.randint(1, 10, size=(4, 4))
A = (A + A.T) // 2  # Make it symmetric
print("Symmetric Matrix A:\n", A)

# Step 2: Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("\nEigenvalues:\n", eigenvalues)
print("\nEigenvectors (columns):\n", eigenvectors)

# Step 3: Check if matrix is diagonalizable
# A symmetric matrix is always diagonalizable
is_diagonalizable = np.linalg.matrix_rank(eigenvectors) == A.shape[0]
print("\nIs the matrix diagonalizable?:", is_diagonalizable)

# Step 4: Sort eigenvalues and corresponding eigenvectors
sorted_indices = np.argsort(eigenvalues)
sorted_eigenvalues = eigenvalues[sorted_indices]
sorted_eigenvectors = eigenvectors[:, sorted_indices]

print("\nSorted Eigenvalues:\n", sorted_eigenvalues)
print("\nCorresponding Sorted Eigenvectors (columns):\n", sorted_eigenvectors)