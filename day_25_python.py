# super method in python 

# super() method  is used to access methods of the parent class 


class car:
    def __init__(self , type):
        self.type = type 

    @staticmethod
    def start():
        print("car started ... ")
        
    @staticmethod
    def stop():
        print(" car stopped ... ")

class toyotacar(car):
    def __init__(self, name, type ):
        super().__init__(type)
        self.name = name 
        super().start()

        
car1 = toyotacar("innova ", " diesel ")
print(car1.type)        


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        super().show()
        print("Class B")

obj = B()
obj.show()



print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# @classmethod decoretor 

# A class method is bound to the class and recevies the class as an implicit first argument 
# note : - static method can't be access or modify class state and generally for utility 

# class attribute change 

class person:
    name = " babalu"

    def changename(self , name):
        # person.name = name # first method 
        self.__class__.name = "vivek"  # second method to access class 

    # @classmethod
    # def changename(cls,name):
    # cls.name = name         ---- this one of the method to access the class attribute or change it ---- it not safe 

p1 = person()
p1.changename("vivek")
print(p1.name)
print(person.name) # it define we also changed original attribute 


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")



class Employee:
    count = 0

    def __init__(self):
        Employee.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

e1 = Employee()
e2 = Employee()
print(Employee.get_count())


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")



class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls, name):
        cls.school = name

s1 = Student()
Student.change_school("NEW  School")
print(s1.school)


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")






