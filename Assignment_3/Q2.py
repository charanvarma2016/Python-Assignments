# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 19:13:17 2025

@author: saikr
"""
"""2. Library Management
Create classes Book, Member, and Library. Implement methods for borrowing and
returning books, checking overdue status, and displaying available books."""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False
    def return_book(self):
        self.is_borrowed = False
    def __str__(self):
        status = "borrowed" if self.is_borrowed else "available"
        return f"{self.title} by {self.author} - {status}"
    
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        
    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is already borrowed")
            
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} has not borrowed {book.title}")
            
    def show_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has no borrowed books")
        else:
            print(f"{self.name} has borrowed:") 
            for book in self.borrowed_books:
              print(f" - {book.title}")
              
class Library:
        def __init__(self, name):
            self.name = name
            self.books = []
            
        def add_book(self, book):
            self.books.append(book)
            
        def show_available_books(self):
            print(f"books available in {self.name}")
            available = [book for book in self.books if not book.is_borrowed]
            if not available:
                print("no books available")
            else:
                for book in available:
                    print(f" - {book}")
                    
lib = Library("city library")
book1 = Book("the alchemist", "paulo")
book2 = Book("harry potter", "j.k.rowling")
book3 = Book("young sheldon", "cooper")

lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)

member1 = Member("charan")

lib.show_available_books()

member1.borrow_book(book1)
member1.borrow_book(book2)

member1.show_borrowed_books()
lib.show_available_books

member1.return_book(book1)
lib.show_available_books()


    
                      
                   
            
        
        