# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 16:25:09 2025

@author: saikr
"""

"""2.Prime Check
Write a function is_prime(n) that checks whether a number is prime.
Example: is_prime(11) → True"""




def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Call the function with a number
print("isprime(4):", is_prime(4))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
