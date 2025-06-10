# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 16:48:02 2025

@author: saikr
"""
"""3. Vehicle Hierarchy
Create a base class Vehicle, and subclasses Car, Motorbike, and Truck. Each subclass
should override a method called vehicle_info() that prints different vehicle
characteristics."""

# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def vehicle_info(self):
        print(f"{self.brand} {self.model} is a generic vehicle.")

# Subclass: Car
class Car(Vehicle):
    def vehicle_info(self):
        print(f"{self.brand} {self.model} is a Car.")
        print(" - 4 wheels")
        print(" - Suitable for families")
        print(" - Comfortable for city and highway drives")

# Subclass: Motorbike
class Motorbike(Vehicle):
    def vehicle_info(self):
        print(f"{self.brand} {self.model} is a Motorbike.")
        print(" - 2 wheels")
        print(" - Great fuel efficiency")
        print(" - Best for solo or duo travel")

# Subclass: Truck
class Truck(Vehicle):
    def vehicle_info(self):
        print(f"{self.brand} {self.model} is a Truck.")
        print(" - 6 or more wheels")
        print(" - Designed for carrying heavy loads")
        print(" - Used in construction and logistics")

# Testing all classes
v = Vehicle("GenericBrand", "ModelX")
c = Car("Toyota", "Camry")
m = Motorbike("Honda", "CBR500R")
t = Truck("Volvo", "FH16")

print("\nVehicle Info:")
v.vehicle_info()

print("\nCar Info:")
c.vehicle_info()

print("\nMotorbike Info:")
m.vehicle_info()

print("\nTruck Info:")
t.vehicle_info()
