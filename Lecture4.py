#           Dictionary & Set
'''
Q1 : WHAT IS DICTIONARY ?
A1 : DICTIONARIES ARE USED TO STORE DATA VALUES IN KEY:VALUE PAIRS.
-> UNORDERED
-> MUTABLE
-> DON'T ALLOW DUPLICATE KEYS

EXAMPLE : DICT1 = {
    "NAME" : "SHRADHA",
    "CGPA" : 9.6,
    "MARKS": [98,97,95]
}
'''
'''
Q2 : HOW TO CHANGE VALUE IN DICTIONARY ?
A2 : DICT1["NAME"] = "VANSH"

Q3 : HOW TO PRINT DICTIONARY ?
A3 : PRINT(DICT1["NAME"])
'''

dictionary = {
    "name" : "Shradha",
    "cgpa" : 9.6,
    "marks": [98,97,95]
}
print(dictionary.items())
print(dictionary.keys())
print(dictionary.values())
dictionary.clear()
print(dictionary)

set1 = {10,20,30,40,50,60,70,80,90,100}
print(type(set1))

set2 = set()
print(type(set2))