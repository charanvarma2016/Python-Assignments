# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 17:49:21 2025

@author: saikr
"""
"""9. Composition
Create a Person class and a Passport class. Use composition to show that each person
has a passport object. Print full passport details through the person instance."""

class Passport:
    def __init__(self, passport_number, nationality, issue_date, expiry_date):
        self.passport_number = passport_number
        self.nationality = nationality
        self.issue_date = issue_date
        self.expiry_date = expiry_date

    def display_passport_details(self):
        print("Passport Details:")
        print(f"  Passport Number: {self.passport_number}")
        print(f"  Nationality: {self.nationality}")
        print(f"  Issue Date: {self.issue_date}")
        print(f"  Expiry Date: {self.expiry_date}")


class Person:
    def __init__(self, name, age, passport):
        self.name = name
        self.age = age
        self.passport = passport  # Composition: Person "has a" Passport

    def display_person_details(self):
        print("Person Details:")
        print(f"  Name: {self.name}")
        print(f"  Age: {self.age}")
        # Accessing passport details through the composition relationship
        self.passport.display_passport_details()


# Example usage:
passport1 = Passport("A1234567", "Canadian", "2022-05-01", "2032-05-01")
person1 = Person("charan", 28, passport1)

person1.display_person_details()

