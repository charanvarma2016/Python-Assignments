# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 18:04:39 2025

@author: saikr
"""
"""11. Inventory System with Inheritance and Composition
Build an inventory system where products can be perishable (expiry date) or non-
perishable. Use inheritance to model types and composition to associate supplier
details."""

from datetime import date

# Supplier class (Composition)
class Supplier:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def get_info(self):
        return f"Supplier: {self.name}, Contact: {self.contact}"


# Base Product class
class Product:
    def __init__(self, name, price, quantity, supplier):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier = supplier  # Composition

    def product_info(self):
        return f"{self.name} - ${self.price} x {self.quantity}\n{self.supplier.get_info()}"


# Perishable Product (inherits Product)
class Perishable(Product):
    def __init__(self, name, price, quantity, supplier, expiry_date):
        super().__init__(name, price, quantity, supplier)
        self.expiry_date = expiry_date

    def is_expired(self):
        return date.today() > self.expiry_date

    def product_info(self):
        status = "Expired" if self.is_expired() else "Valid"
        return super().product_info() + f"\nExpiry Date: {self.expiry_date} ({status})"


# NonPerishable Product (inherits Product)
class NonPerishable(Product):
    def __init__(self, name, price, quantity, supplier):
        super().__init__(name, price, quantity, supplier)

    # No expiry, so just use base product_info
    def product_info(self):
        return super().product_info() + "\nType: Non-Perishable"


# Example
if __name__ == "__main__":
    supplier1 = Supplier("Fresh Farms", "123-456-7890")
    supplier2 = Supplier("Tech Supplies", "987-654-3210")

    apple = Perishable("Apple", 0.5, 100, supplier1, date(2025, 6, 5))
    keyboard = NonPerishable("Keyboard", 25.0, 50, supplier2)

    inventory = [apple, keyboard]

    for item in inventory:
        print(item.product_info())
        print("-" * 40)