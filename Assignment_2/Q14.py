# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 16:22:41 2025

@author: saikr
"""
"""14.Leap Year Checker
Write a program that checks if a given year is a leap year or not.
(A year is a leap year if it is divisible by 4, but not by 100 unless also divisible by 400.)"""

def is_leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


year_input = int(input("Enter a year: "))
is_leap_year(year_input)
