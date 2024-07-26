""" numbers = [1,2,3,4,5]

while (n := len(numbers)) > 0:
    print(numbers.pop())
    
print(numbers) """

""" happy = False
print(happy)

print(happy := True) """

# aam zindagi
""" foods = list()
while True:
    food = input("What food do u like ? : ")
    if food == "quit":
        break
    foods.append(foods)  """

# Mentos zindagi
""" foods = list()
while (food := input("Which food do u like ?: ")) != "quit":
    foods.append(food) """
    
    
# aam zindagi
""" number = int(input("Enter any number to check it is divisible by 7 :"))

if number % 7 == 0:
    print("Divisible")
else:
    print("Not Divisible") """
    
# Mentos zindagi
if (number := int(input("Enter any number to check it is divisible by 7 :"))) % 7 == 0:
    print("Divisible")
else:
    print("Not Divisible")