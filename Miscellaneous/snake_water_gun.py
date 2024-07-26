import random
comp = random.randint(0,2)
user = int(input("Enter 0 for snake, 1 for water, 2 for gun :"))

if comp == user:
    print("It's Draw")
elif comp == 0 and user == 1:
    print("Computer Won!")
elif comp == 1 and user == 2:
    print("Computer Won")
elif comp == 2 and user == 0:
    print("Computer Won!")
else:
    print("Invalid")