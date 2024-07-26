# MAP

sq = [1,2,3,4,5]

def square(x):
    return x*x

print(list(map(square,sq)))

# FILTER

a = [10,20,30,40,50]

def filterfunction(x):
    return x>20

print(list(filter(filterfunction,a))) 
