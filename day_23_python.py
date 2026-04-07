# del keyword used to delete object properties and delete object itself 

class Student:

    def __init__(self, name):
        self.name = name

s1 = Student("Vivek")
print(s1.name)


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")

del s1
print(s1)

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# Private (like) attribute and methods 
# conceptual implementation in python
# private attribute and methods are meant to be used only within the class and are not accessible for outside the class 


