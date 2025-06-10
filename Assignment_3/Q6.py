# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 17:11:44 2025

@author: saikr
"""
"""6. E-Commerce Cart
Create classes Product, CartItem, and ShoppingCart. Implement add/remove items,
calculate total price, and apply discounts."""

# Product class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# CartItem class
class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product.price * self.quantity


# ShoppingCart class
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        # Check if item already in cart
        for item in self.items:
            if item.product.name == product.name:
                item.quantity += quantity
                print(f"Added {quantity} more of {product.name} to cart.")
                return
        self.items.append(CartItem(product, quantity))
        print(f"Added {product.name} (x{quantity}) to cart.")

    def remove_item(self, product_name):
        for item in self.items:
            if item.product.name == product_name:
                self.items.remove(item)
                print(f"Removed {product_name} from cart.")
                return
        print(f"{product_name} not found in cart.")

    def calculate_total(self):
        total = sum(item.get_total_price() for item in self.items)
        return total

    def apply_discount(self, discount_percent):
        total = self.calculate_total()
        discount = total * (discount_percent / 100)
        final_total = total - discount
        print(f"Discount applied: {discount_percent}%")
        print(f"Discount amount: ${discount:.2f}")
        return final_total

    def display_cart(self):
        if not self.items:
            print("Cart is empty.")
            return
        print("Items in Cart:")
        for item in self.items:
            print(f"- {item.product.name} (x{item.quantity}) - ${item.get_total_price():.2f}")
        print(f"Total: ${self.calculate_total():.2f}")
        
# Creating products
p1 = Product("Laptop", 1200)
p2 = Product("Mouse", 25)
p3 = Product("Keyboard", 45)

# Creating a shopping cart
cart = ShoppingCart()

# Adding items
cart.add_item(p1, 1)
cart.add_item(p2, 2)
cart.add_item(p3, 1)

# Display cart
print("\n--- CART DETAILS ---")
cart.display_cart()

# Apply discount
print("\n--- APPLYING DISCOUNT ---")
final_amount = cart.apply_discount(10)  # 10% discount
print(f"Final Price after discount: ${final_amount:.2f}")

# Removing an item
print("\n--- REMOVING ITEM ---")
cart.remove_item("Mouse")
cart.display_cart()
