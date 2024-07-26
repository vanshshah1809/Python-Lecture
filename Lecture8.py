# OOPS CONCEPT
'''
class Student:
    college = "Gujarat University"
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def welcome(self):
        print(f"Good Morning {self.name} !, Welcome to {self.college}, your marks is : {self.marks}")

x = input("Enter Your Name :")
y = int(input("Enter Your Total Marks :"))

en120 = Student(x,y)
en120.welcome()
'''

# Practice Answer

'''class Student:
    def __init__(self,name,english,hindi,math):
        self.name = name
        self.english = english
        self.hindi = hindi
        self.math = math
    
    def display(self):
        avg = (self.english + self.hindi + self.math) / 3
        print(f"Hello {self.name}! Your Average Score = {avg}")
    
    @staticmethod    
    def greetings():
        print("Good Morning Sir!")
        
s120 = Student("Vansh",97,98,99)
s120.greetings()
s120.display()
'''

# Practice Answer 2

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
    
    def debit(self,amount):
        self.balance = self.balance - amount
        print(f"{amount}/- deducted from your account no: {self.account_no}")
        print(f"Your Total Available balance is {self.display_balance()}")
    
    def credit(self,amount):
        self.balance = self.balance + amount
        print(f"{amount} has been credited to your account no: {self.account_no}")
        print(f"Your Total Available balance is {self.display_balance()}")
    
    def display_balance(self):
        if (self.balance < 1000):
            print("Low Balance")
            return self.balance
        else:
            return self.balance
    
cust1 = Account(10000, 81700)
cust1.debit(5000)
cust1.credit(7500)
cust1.credit(18000)
cust1.debit(30000)