class Account:
    def __init__(self,acc_no,bal):
        self.account_number = acc_no
        self.balance = bal
    
    def debit(self,amt):
        self.amount = amt
        self.balance = self.balance - self.amount
        print(f"{self.amount}/- has been deducted from your bank account number : {self.account_number}")
        print(f"Updated balance for your account number : {self.account_number} is {self.balance}")
    
    def credit(self,amount):
        self.amount = amount
        self.balance = self.balance + amount
        print(f"Your account has been credited by {self.amount}/-")
        print(f"Updated Balance for your account number is {self.balance}/-")
    
cust1 = Account(123789,15000)
cust2 = Account(123987,30000)
cust3 = Account(123654,55000)

cust1.debit(5000)

class student:
    def __init__(self, name):
        self.name = name
        print(f"Welcome {self.name}")

s1 = student("Vansh")
s2 = student("Manya")

print("-------------------------------------------------")

class Account1:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    
    def info(self):
        print(self.__acc_pass)
        
cust1 = Account1(12345,"abcde")
print(cust1.acc_pass)
cust1.info()