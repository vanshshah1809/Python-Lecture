x = [1,2,3,4,5]
print(dir(x))

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name)
    
p1 = person("Rahul Kumar", 21)
print(p1.__dict__)
