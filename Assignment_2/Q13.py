# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 16:13:55 2025

@author: saikr
"""
"""13.Pattern Printer
Create a function print_pattern(n) that prints this pattern:

1
1 2
1 2 3
...
1 2 3 ... n"""

def print_pattern(n):
    for i in range(1, n + 1):          # Loop from 1 to n
        for j in range(1, i + 1):      # Print numbers from 1 to i
            print(j, end=" ")          # Print on same line with space
        print()                        # Move to the next line after each row

# Example usage
print_pattern(5)
