#                   STRINGS AND CONDITIONAL STATEMENTS
'''
Q1: WAP TO CHECK IF A NUMBER ENTERED BY THE USER IS ODD OR EVEN
Q2: WAP TO FIND GREATEST OF 3 NUMBERS ENTERED BY THE USER
Q3: WAP TO CHECK IF A NUMBER IS A MULTIPLE OF 7 OR NOT
'''
# A1:
num = int(input("Enter any number :"))
if(num % 2 == 0):
    print("Even")
else:
    print("Odd")

# A2:
num1 = int(input("Enter First Number :"))
num2 = int(input("Enter Second Number :"))
num3 = int(input("Enter Third Number :"))

if (num1 > num2):
    if(num1 > num3):
        print(num1)
    else:
        print(num3)
else:
    if(num2 > num3):
        print(num2)
    else:
        print(num3)
        
# A3:
table = int(input("Enter any number :"))

if(table % 7 == 0):
    print("Yes!, It is multiple of 7")
else:
    print("No!, It is not multiple of 7")
    
    