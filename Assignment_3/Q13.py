# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 17:17:16 2025

@author: saikr
"""
"""13. Event Management System
Design a system where multiple Events can be created. Each event can have different
types of Attendees (e.g., VIP, Guest, Staff). Use polymorphism and class methods to
handle registration and seating logic."""


# Base class for Attendee
class Attendee:
    def __init__(self, name):
        self.name = name

    def get_seating(self):
        return "General Area"

    def __str__(self):
        return f"{self.name} ({self.__class__.__name__}) - Seat: {self.get_seating()}"


# Subclasses for different attendee types
class VIP(Attendee):
    def get_seating(self):
        return "Front Row VIP Lounge"


class Guest(Attendee):
    def get_seating(self):
        return "Middle Row Guest Area"


class Staff(Attendee):
    def get_seating(self):
        return "Staff Backstage Access"


# Event class
class Event:
    def __init__(self, name):
        self.name = name
        self.attendees = []

    def register_attendee(self, attendee):
        self.attendees.append(attendee)
        print(f"{attendee.name} registered as {attendee.__class__.__name__}")

    def show_attendee_list(self):
        print(f"\nEvent: {self.name}")
        print("Attendee List & Seating:")
        for attendee in self.attendees:
            print(f" - {attendee}")


# Example
if __name__ == "__main__":
    # Create an event
    concert = Event("Summer Music Fest")

    # Create attendees
    a1 = VIP("Alice")
    a2 = Guest("Bob")
    a3 = Staff("Charlie")
    a4 = Guest("David")
    a5 = VIP("Eve")

    # Register attendees
    concert.register_attendee(a1)
    concert.register_attendee(a2)
    concert.register_attendee(a3)
    concert.register_attendee(a4)
    concert.register_attendee(a5)

    # Display seating and attendees
    concert.show_attendee_list()