# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 17:31:16 2025

@author: saikr
"""
"""7. Encapsulation Example
Create a class Student with private attributes for marks. Provide getter/setter methods
with validation logic to ensure marks are between 0 and 100."""

class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = 0  # private attribute

    # Getter method
    def get_marks(self):
        return self.__marks

    # Setter method with validation
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print(f"Marks updated to {marks} for {self.name}")
        else:
            print("Invalid marks! Please enter a value between 0 and 100.")

    # Display method
    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.__marks}")
        
# Creating a Student object
s1 = Student("Charan")

# Trying to set valid marks
s1.set_marks(85)

# Trying to set invalid marks
s1.set_marks(110)

# Getting marks
print("Retrieved Marks:", s1.get_marks())

# Display student info
print("\n--- Student Info ---")
s1.display_info()
