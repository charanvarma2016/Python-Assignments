#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 14:01:26 2025

@author: charan
"""
import numpy as np
import time

# Create two large 1D arrays of size 1 million with random values between 1 and 100
size = 1_000_000
arr1 = np.random.randint(1, 101, size)
arr2 = np.random.randint(1, 101, size)

# Function to do element-wise operations using loops
def loop_operations(a, b):
    add_res = np.empty_like(a)
    sub_res = np.empty_like(a)
    mul_res = np.empty_like(a)
    for i in range(len(a)):
        add_res[i] = a[i] + b[i]
        sub_res[i] = a[i] - b[i]
        mul_res[i] = a[i] * b[i]
    return add_res, sub_res, mul_res

# Measure time for loop method
start_time = time.time()
add_loop, sub_loop, mul_loop = loop_operations(arr1, arr2)
loop_time = time.time() - start_time

# Measure time for vectorized method
start_time = time.time()
add_vec = arr1 + arr2
sub_vec = arr1 - arr2
mul_vec = arr1 * arr2
vec_time = time.time() - start_time

# Verify the results are the same
print("Addition equal:", np.array_equal(add_loop, add_vec))
print("Subtraction equal:", np.array_equal(sub_loop, sub_vec))
print("Multiplication equal:", np.array_equal(mul_loop, mul_vec))

# Print timing results
print(f"Loop method time: {loop_time:.4f} seconds")
print(f"Vectorized method time: {vec_time:.4f} seconds")

# Explanation
if vec_time < loop_time:
    print("\nVectorized operations are faster because NumPy uses optimized C code and avoids explicit Python loops.")
else:
    print("\nLoop operations are faster (this is rare; usually vectorization wins).")
