# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 17:20:00 2025

@author: saikr
"""
"""14. Mini ATM Simulation
Simulate an ATM machine. Use classes to model ATM, Bank, and Account. Implement
pin validation, withdrawal, deposit, balance inquiry, and transaction history."""

class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            print(f"Deposit successful. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            print(f"Withdrawal successful. New balance: ${self.balance}")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")
        return self.balance

    def show_transaction_history(self):
        print("\nTransaction History:")
        if self.transaction_history:
            for t in self.transaction_history:
                print(f" - {t}")
        else:
            print("No transactions found.")


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def authenticate(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            return account
        else:
            return None


class ATM:
    def __init__(self, bank):
        self.bank = bank

    def start(self):
        print("=== Welcome to the ATM ===")
        acc_num = input("Enter account number: ")
        pin = input("Enter PIN: ")

        account = self.bank.authenticate(acc_num, pin)
        if not account:
            print("Authentication failed.")
            return

        while True:
            print("\n--- ATM Menu ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transaction History")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                account.check_balance()
            elif choice == "2":
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == "3":
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif choice == "4":
                account.show_transaction_history()
            elif choice == "5":
                print("Thank you for using the ATM.")
                break
            else:
                print("Invalid option. Try again.")


# Example
if __name__ == "__main__":
    # Create bank and add sample accounts
    bank = Bank()
    bank.add_account(Account("12345", "1111", 1000))
    bank.add_account(Account("54321", "2222", 500))

    # Create ATM and start interaction
    atm = ATM(bank)
    atm.start()
