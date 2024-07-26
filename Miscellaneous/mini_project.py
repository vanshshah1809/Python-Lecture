class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        
    @property
    def percentage(self):
        return (self.phy + self.chem + self.math) / 3
        
s1 = Student(98,99,97)
s1.math = 99
print(s1.percentage)