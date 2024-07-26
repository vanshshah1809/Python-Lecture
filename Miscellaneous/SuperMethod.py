class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
class Programmer(Employee):
    def __init__(self,name, id, lang):
        super().__init__(name, id)
        self.lang = lang

p1 = Programmer("Rohan", 123, "Python")
print(p1.name)
print(p1.id)
print(p1.lang)