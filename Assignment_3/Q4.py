# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 16:58:29 2025

@author: saikr
"""
"""4. Polymorphism in Action
Create a base class Animal with a method make_sound(). Create child classes like
Dog, Cat, and Cow that override this method. Write a loop that calls this method on a list
of mixed animal objects."""

# Base class
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

# Subclass Dog
class Dog(Animal):
    def make_sound(self):
        print("Dog says: Woof!")

# Subclass Cat
class Cat(Animal):
    def make_sound(self):
        print("Cat says: Meow!")

# Subclass Cow
class Cow(Animal):
    def make_sound(self):
        print("Cow says: Moo!")

animals = [Dog(), Cat(), Cow(), Dog(), Cow()]

# Loop through the list and call make_sound()
print("Animal Sounds:")
for animal in animals:
    animal.make_sound()
