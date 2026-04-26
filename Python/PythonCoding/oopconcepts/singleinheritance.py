#Parent Class
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print("Name:",self.name)
        print("Salary:",self.salary)

# Child Class
class Manager(Employee):
    def __init__(self,name,salary,department):
        #calling parent constructor
        super().__init__(name,salary)
        self.department = department

    def show_manager(self):
        print("Department:",self.department)


#Driver Code
m1 = Manager("Ayush",50000,"IT")

m1.show_details() #inherited method
m1.show_manager() # child method
