# create student class that makes name and marks of 3 subject as argument in constructor 
# then create a method to print the avrage



class student:

    def __init__(self, marks, name):
        self.marks = marks
        self.name = name

    def get_avg(self):
        total = 0
        for val in self.marks:
            total += val
        print("Hello", self.name, "your avg is:", total / len(self.marks))


s1 = student([97, 98, 99], "vivek")   # ✔ correct order
s1.get_avg()

s1.name = " babalu "
s1.get_avg()

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")



# create a class to get students average by using their marks 

class Student:
    def __init__(self, sname, smarks):
        self.name = sname
        self.marks = smarks

    def get_average(self):
        total = 0
        for m in self.marks:
            total += m
        avg = total / len(self.marks)
        print("Name:", self.name)
        print("Average Marks:", avg)

ss1 = Student("Vivek", [80, 90, 85])
ss1.get_average()



print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# create a class to fine rectangle area and parameter 

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

r1 = Rectangle(10, 5)
print("Area:", r1.area())
print("Perimeter:", r1.perimeter())



print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# create a simple calculator using class and object creation 

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print("Sum:", self.a + self.b)

    def multiply(self):
        print("Multiplication:", self.a * self.b)

calc = Calculator(5, 3)
calc.add()
calc.multiply()