# Parent Class 1
class Employee:
    def __init__(self,name):
        self.name = name

    def show_name(self):
        print("Name:",self.name)

# Parent Class 2
class Salary:
    def __init__(self,salary):
        self.salary = salary

    def show_salary(self):
        print("Salary:", self.salary)


# Child Class ( Multiple Inheritance )
class Manager(Employee, Salary):
    def __init__(self, name, salary, dept):
        Employee.__init__(self, name)
        Salary.__init__(self, salary)
        self.dept = dept

    def show_all(self):
        self.show_name()
        self.show_salary()
        print("Department:",self.dept)

# Driver Code
m = Manager("Ayush", 50000, 'IT')

print("\n Multiple Inheritance")
m.show_all()