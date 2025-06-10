# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 17:03:28 2025

@author: saikr
"""
"""5. Employee Management System
Build a system with classes for Employee, Developer, and Manager. Include methods to
calculate salary, apply bonuses, and display employee details."""

# Base class
class Employee:
    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

    def apply_bonus(self, bonus):
        self.base_salary += bonus
        print(f"Bonus of {bonus} applied to {self.name}")

    def display_details(self):
        print(f"Name       : {self.name}")
        print(f"ID         : {self.emp_id}")
        print(f"Salary     : {self.base_salary}")


# Subclass: Developer
class Developer(Employee):
    def __init__(self, name, emp_id, base_salary, programming_language):
        super().__init__(name, emp_id, base_salary)
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()
        print(f"Role       : Developer")
        print(f"Language   : {self.programming_language}")


# Subclass: Manager
class Manager(Employee):
    def __init__(self, name, emp_id, base_salary, department):
        super().__init__(name, emp_id, base_salary)
        self.department = department

    def display_details(self):
        super().display_details()
        print(f"Role       : Manager")
        print(f"Department : {self.department}")


dev = Developer("Alice", 101, 60000, "Python")
mgr = Manager("Bob", 201, 80000, "Sales")

# Display initial details
print("=== Developer Details ===")
dev.display_details()

print("\n=== Manager Details ===")
mgr.display_details()

# Apply bonuses
dev.apply_bonus(5000)
mgr.apply_bonus(10000)

# Display updated salary
print("\n=== Updated Developer Details ===")
dev.display_details()

print("\n=== Updated Manager Details ===")
mgr.display_details()
