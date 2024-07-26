class Person:
    name = 'anonymous'
    
    @classmethod
    def changeName(self, name):
        self.name = name
        print(self.name)
                
p1 = Person()
p1.changeName("Sourav")
print(Person.name)