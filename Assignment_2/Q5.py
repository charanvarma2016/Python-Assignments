# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 17:36:30 2025

@author: saikr
"""
"""5.Fibonacci Sequence Generator
Write a function generate_fibonacci(n) that returns a list of first n Fibonacci numbers.
Example: generate_fibonacci(6) → [0, 1, 1, 2, 3, 5]"""


def generate_fibonacci(n):
    if n <= 0:
        return []  
    elif n == 1:
        return [0]  
    
    fib_seq = [0, 1]  # Starting list with first two Fibonacci numbers
    
    while len(fib_seq) < n:
        next_num = fib_seq[-1] + fib_seq[-2]  # Sum of last two numbers
        fib_seq.append(next_num)
    
    return fib_seq


print(generate_fibonacci(7))  