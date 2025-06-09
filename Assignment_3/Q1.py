# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 17:36:52 2025

@author: saikr
"""
"""1. Bank System
Design a BankAccount class with deposit, withdraw, and balance methods. Create two
child classes: SavingsAccount and CurrentAccount with their own withdrawal limits or
overdraft rules."""

class BankAccount():
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit amount ${amount}, new balance: ${self.balance}")
        else:
            print("Amount must be positive")
            
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficiant balance")
        else:
            self.balance -= amount
            print(f"whthdraw amount ${amount}, new balance: ${self.balance}")
            
    def balance(self):
        return self.balance
    
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, withdraw_limit = 10000):
        super().__init__(account_holder, balance)
        self.withdraw_limit = withdraw_limit
        
    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print(f"amount exceeds withdraw limt of ${amount}")
        elif amount > self.balance:
            print("insufficiant balance")
        else:
            self.balance -= amount
            print(f"withdrew amount is ${amount}, new balance: ${self.balance}")
            
class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=400):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit
        
    def overdraft_limit(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print(f"overdraft limit exceeded. Max overdraft limit: ${self.balance+self.overdraft_limit}")
        else:
            self.balance -= amount
            print(f"withdrew amount is $(amount), new balance: ${self.balance}")
            
savings = SavingsAccount("charan", balance=1000)
current = CurrentAccount("Varma", balance=500)

savings.deposit(500)
savings.withdraw(200)
savings.withdraw(15000)

current.withdraw(200)
current.withdraw(1000)

           
    
    
    
        
        
            
        
        
