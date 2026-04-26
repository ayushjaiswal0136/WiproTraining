'''
Employee Management System You are developing an employee management system for a company.
 Implement a class called Employee with the following specifications:
 The class should have private instance variables for employee ID, name, and salary.
 Include a constructor to initialize these variables. Implement getter and setter
 methods for each instance variable. Implement a method to display employee information.
Implement a method to give a salary hike to an employee.
The method should accept a percentage value by which the salary will be increased.
Write a Python program to demonstrate the functionality of the Employee class by creating instances,
 displaying employee information, giving salary hikes, and displaying updated employee information.
'''

class Employee:

    # Constructor
    def __init__(self, employee_id, name, salary):
        self.__employee_id = employee_id
        self.__name = name
        self.__salary = salary

    # Property: employee_id
    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, value):
        self.__employee_id = value

    # Property: name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    # Property: salary
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self.__salary = value
        else:
            print("Salary cannot be negative.")

    # Displaying employee info
    def display_info(self):
        print("EMPLOYEE DETAILS")
        print(f"Employee ID : {self.employee_id}")
        print(f"Name        : {self.name}")
        print(f"Salary      : Rs.{self.salary:.2f}")

    # Salary hike method
    def give_hike(self, percentage):
        if percentage <= 0:
            print("Hike percentage must be positive.")
        else:
            hike_amount = (percentage / 100) * self.__salary
            self.__salary += hike_amount
            print(f"{percentage}% hike applied. Hike Amount: Rs.{hike_amount:.2f}")


# Driver Code
print("EMPLOYEE MANAGEMENT SYSTEM")

# Creating employee objects
emp1 = Employee("EMP0310", "Ayush Jaiswal", 50000)
emp2 = Employee("EMP2608", "Shreya Rastogi", 65000)

# Displaying info
print("\nEmployee 1 Details:")
emp1.display_info()

print("\nEmployee 2 Details:")
emp2.display_info()

# Giving salary hike
print("\nGiving 20% hike to Ayush Jaiswal...")
emp1.give_hike(20)
emp1.display_info()

print("\nGiving 15% hike to Shreya Rastogi...")
emp2.give_hike(15)
emp2.display_info()

# Using setter
print("\nUpdating Employee 1 name...")
emp1.name = "Ansh Jaiswal"
emp1.display_info()

# Using getter
print("\nFetching Employee 2 details:")
print(f"ID     : {emp2.employee_id}")
print(f"Name   : {emp2.name}")
print(f"Salary : Rs.{emp2.salary:.2f}")