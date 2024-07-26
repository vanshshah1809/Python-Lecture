'''class Bank_Account:
    amount = 0
    
    def __init__(self, status, amount):
        self.status = status
        self.amount = amount
        
    def deposit(self, new_amount):
        self.new_amount = new_amount
        self.amount = self.new_amount + self.amount
        
    def display_balance(self):
        print(f"Amount = {self.amount}")


cust1 = Bank_Account("Account Opened",20000)
cust1.deposit(15000)
cust1.display_balance()
print(f"Class Amount = {Bank_Account.amount}")

cust2 = Bank_Account("Account Opened",40000)
cust2.deposit(10000)
cust2.display_balance()
print(Bank_Account.amount)'''

'''class circle:
    def __init__(self, r):
        self.r = r
    
    def area(self):
        self.area_of_circle = (22/7) * self.r * self.r
        print(f"Area of circle :{self.area_of_circle}")
    
    def parameter(self):
        self.parameter_of_circle = 2 * (22/7) * self.r
        print(f"Parimeter of Circle :{self.parameter_of_circle}")
    
obj1 = circle(20)
obj1.area()
obj1.parameter()'''
'''
class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
        
    def showDetails(self):
        print(f"Role : {self.role}")
        print(f"Department : {self.department}")
        print(f"Salary : {self.salary}")
        
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Data Scientist", "IT", 75000)
        
    def DisplayDetails(self):
        print(f"Name :{self.name}")
        print(f"Age :{self.age}")
        return super().showDetails()
    
obj1 = Engineer("Rahul Kumar", 21)
obj1.DisplayDetails()'''


class Device:
    def __init__(self, name, manufacturer, price):
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        
    def device_details(self):
        print(f"Name : {self.name}")
        print(f"Manufacturer : {self.manufacturer}")
        print(f"Price : {self.price}")
    
class Laptop(Device):
    def __init__(self, processor):
        self.processor = processor
    
    def laptop_details(self):
        print(f"Name : {self.name}")
        print(f"Manufacturer : {self.manufacturer}")
        print(f"Price : {self.price}")
        print(f"processor : {self.processor}")

class Mobile(Laptop):
    def __init__(self, storage, ram):
        self.storage = storage
        self.ram = ram
        
    def mobile_details(self):
        print(f"Name : {self.name}")
        print(f"Manufacturer : {self.manufacturer}")
        print(f"Price : {self.price}")
        print(f"processor : {self.processor}")
        print(f"Ram : {self.ram}")
        print(f"Storage : {self.storage}")

obj1 = Mobile("128 gb","6gb")
obj1.device_details()