# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 15:50:56 2025

@author: saikr
"""
"""11.Grade Calculator
Write a program that takes a student's score (0–100) as input and prints the grade:
● 90–100: A
● 80–89: B
● 70–79: C
● 60–69: D
● <60: F"""


def calculate_grade(score):
    if score >= 90 and score <= 100:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    elif score >= 0:
        print("Grade: F")
    else:
        print("Invalid score. Please enter a number between 0 and 100.")


try:
    user_score = int(input("Enter your score (0–100): "))
    calculate_grade(user_score)
except ValueError:
    print("Invalid input. Please enter a number.")