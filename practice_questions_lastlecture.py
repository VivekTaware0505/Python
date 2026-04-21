# que no 1 :  define a circle class to create a circle with radius r using the constructor define an Area()
# method of the class which calculates the area of the circle define a perimeter() method of the class 
# which allows you to calculate the perimeter of the circle 


class circle:
    def __init__(self, radius):
        self.radius  = radius

    def area(self):
        return(22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    

c1 = circle(21)
print(c1.area())
print(c1.perimeter())



print("-------------------------------------- vivek learning python -----------------------------------------------------------")
print("-------------------------------------- vivek learning python -----------------------------------------------------------")


# Q2 define a employee class with attribute role department and salary this class has a also showdetails() method 
# create an engineer class that inherits propeties from employee  and has additional attributes : name and age 

class employee:
    def __init__(self, dep , role , salary):
        self.role = role
        self.dep = dep
        self.salary = salary 

    def showdetail(self):
        print(" Role  = ", self.role)
        print("Department = ", self.dep)
        print(" salary = ", self.salary)

class engineer(employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__(" engineer", " IT ", " 75000")

eg1 =  engineer("vivek", " 22")
eg1.showdetail()





