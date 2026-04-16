# property 
# we use @porpety decorator on any method in the class the method as a property 

class student:
    def __init__(self, phy, chem, math ):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) +" % "

stu1 = student( 98, 59, 94)

print(stu1.percentage)     

stu1.chem = 91
print(stu1.percentage)