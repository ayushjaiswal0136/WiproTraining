'''
Use class, objects, constructors while coding Bank Account Management System You are tasked with
creating a simple bank account management system in Python. Implement a class called BankAccount
 with the following specifications: The class should have private instance variables for
  account number, account holder name, and balance. Include a constructor to initialize these variables.
  Implement getter and setter methods for each instance variable to ensure encapsulation.
   Implement methods to deposit and withdraw money from the account.
   Ensure that the withdraw method checks if the account has sufficient balance before allowing withdrawal.
    Write a Python program to demonstrate the functionality of the BankAccount class by creating instances,
    depositing and withdrawing money, and displaying account information.
'''

class BankAccount:

    # Constructor
    def __init__(self, account_number, holder_name, balance=0):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance

    # Property: account_number
    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, value):
        self.__account_number = value

    # Property: holder_name
    @property
    def holder_name(self):
        return self.__holder_name

    @holder_name.setter
    def holder_name(self, value):
        self.__holder_name = value

    # Property: balance
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("Balance cannot be negative.")

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Rs.{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    # Withdraw method
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance! Withdrawal denied.")
        else:
            self.__balance -= amount
            print(f"Rs.{amount} withdrawn successfully.")

    # Display method
    def display_info(self):
        print("\nACCOUNT DETAILS")
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.holder_name}")
        print(f"Balance        : Rs.{self.balance}")


# Driver Code
print("BANK ACCOUNT MANAGEMENT SYSTEM")

acc1 = BankAccount("ACS0310", "Ayush Jaiswal", 10000)
acc1.display_info()

print("\nDepositing Rs.5000...")
acc1.deposit(5000)
acc1.display_info()

print("\nWithdrawing Rs.3000...")
acc1.withdraw(3000)
acc1.display_info()

print("\nTrying to withdraw Rs.20000...")
acc1.withdraw(20000)

print("\nUpdating account holder name...")
acc1.holder_name = "Ansh Jaiswal"   # setter
acc1.display_info()

print("\nChecking balance using getter:")
print("Balance:", acc1.balance)   # getter