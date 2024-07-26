#           List & Tuples
'''
Q1 : WHAT IS LISTS ?
A1 : A BUILT-IN DATATYPE THAT STORES SET OF VALUES. IT IS A MUTABLE DATATYPE.
'''

list7 = [10,30,20,40,50]

list7.append(60)
list7.sort()
list7.sort(reverse = True)
list7.reverse()
list7.insert(1,99)
list7.remove(99)
print(list7)

'''
Q2 : WHAT IS TUPLE ?
A2 : A BUILT-IN DATATYPE THAT LET US CREATE IMMUTABLE SEQUENCE OF VALUE. 
     IT IS IMMUTABLE DATATYPE.
'''
tup = (10,10,20,30,40,50)

# tup[1] = 99 tuple does not support item assignment
print(f"Element 10 presents {tup.count(10)} times")

print(tup)

# PRACTICE QUESTIONS
'''
Q1 : WAP TO ASK THE USER TO ENTER NAMES OF THEIR 3 FAVOURITE MOVIES
     & STORE THEM IN A LIST.
'''
# A1 :
a = input("Enter first movie name :")
b = input("Enter second movie name :")
c = input("Enter third movie name :")

movies = []

movies.append(a)
movies.append(b)
movies.append(c)

print(movies)

'''
Q2 : WAP TO CHECK IF A LIST CONTAINS A PALINDROME OF ELEMENTS OR NOT
'''

# A2 :
list1 = [10,20,10]
list2 = list1.copy()
print(f"List1 : {list1}")
print(f"List2 : {list2}")

list2.reverse()
print(list2)

if list1 == list2:
    print("Palindrom")
else:
    print("Not Palindrom")

'''
Q3 : WAP TO COUNT THE NUMBER OF STUDENTS WITH THE "A" GRADE IN THE FOLLOWING TUPLE.
'''
# A3 :

tuple1 = ("C","D","A","A","B","B","A")
a = tuple1.count("A")
print(f"Count Of Students With A Grade {a}")

'''
Q4 : STORE THE ABOVE VALUES IN A LIST & SORT THEM FROM A TO D.
'''

ab = list(tuple1)
print(ab)

ab.sort()
print(ab)