#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 13:33:24 2025

@author: charan
"""
import numpy as np
import matplotlib.pyplot as plt

# Generate a 1000x1000 matrix with Gaussian distribution (mean=0, std=1)
matrix = np.random.normal(loc=0, scale=1, size=(1000, 1000))

# Compute mean and standard deviation
matrix_mean = np.mean(matrix)
matrix_std = np.std(matrix)

# Print mean and standard deviation
print("Mean of matrix:", matrix_mean)
print("Standard deviation of matrix:", matrix_std)

# Visualize distribution using a histogram
plt.hist(matrix.ravel(), bins=100, color='skyblue', edgecolor='black')
plt.title("Histogram of 2D Gaussian Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
