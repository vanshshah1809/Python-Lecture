print("-----------------------------------------------")
print("Press 1 to capitalize your string")
print("Press 2 to lower your string")
print("Press 3 to upper your string")
print("Press 4 to casefold your string")
print("-----------------------------------------------")

Word = input("Enter any word you want :")
choice = int(input("Enter your choice :"))

def Capital():
    cap = Word.capitalize()
    print(cap)
    
def Lower():
    sm = Word.lower()
    print(sm)

def Upper():
    up = Word.upper()
    print(up)

def CaseFold():
    cf = Word.casefold()
    print(cf)

if choice == 1:
    Capital()
elif choice == 2:
    Lower()
elif choice == 3:
    Upper()
elif choice == 4:
    CaseFold()
else:
    print("Invalid Input !")