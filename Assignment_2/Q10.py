# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 15:43:48 2025

@author: saikr
"""
"""10.Even or Odd Checker
Write a Python program that takes a number as input and prints whether it's even or odd."""


def even_or_odd(n):
    if n % 2 == 0:
        print(f"{n}is even.")
    else:
        print(f"{n} is odd.")


number = int(input("Enter a number: "))
even_or_odd(number)
