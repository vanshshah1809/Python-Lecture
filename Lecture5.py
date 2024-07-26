#                   LOOPS
'''
-> LOOPS ARE USED TO REPEAT INSTRUCTIONS
-> THERE ARE TWO TYPES OF LOOPS : 1) WHILE LOOP
                                  2) FOR   LOOP                            
'''
'''
# WHILE LOOP :->
count = 1
while count<=5:
    print("hello",count)
    count += 1
    
alphabets = ["A","B","C","D"]
i = 0
while i<len(alphabets):
    print(alphabets[i])
    i = i + 1

# Q1 : FIND 36 IN THE FOLLOWING TUPLE

tup = (10,20,36,40,50,60,70,80,36,100)
target = 36

i = 0
while i < len(tup):
    if tup[i] == target:
        print(f"Element {target} Found at index {i}")
    i += 1

#Q2 : FIND ODD NUMBERS FROM THE FOLLOWING TUPLE

odd = (1,2,3,4,5,6,7,8,9,9,10)
i=0
while i < len(odd):
    if odd[i] % 2 != 0:
        print(odd[i])
    i += 1
    
'''

"""
EXERCISE
Q1 : PRINT NUMBERS FROM 1 TO 100 (FOR LOOP)
Q2 : PRINT NUMBERS FROM 100 TO 1 (FOR LOOP)
Q3 : PRINT MULTIPLICATION TABLE OF THE NUMBER ENTERED BY USER
"""

# A1:
for i in range(1,101):
    print(i)
# A2:
for i in range(100,0,-1):
    print(i)
# A3:
table = int(input("Enter the number of which table u want :"))

for i in range(1,11):
    print(f"{table} x {i} = {table * i}")