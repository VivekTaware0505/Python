# object oriented using pyhton part -01

class student:
    name = "Vivek"



v1 = student()
print(v1.name)


v2 = student()
print(v2.name)

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# example of car factory 

class Car:
    color = " blue"
    brandname = "TATA"

car1 = Car()
print("car 1 : ",car1.color, car1.brandname)

car2 = Car()
print("car 2 : ",car2.color)

car3 = Car()
print("car 3 : ",car3.color)


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# init function in class and object 

class college:
    new_name = "vivek taware"
    def __init__(self,fullname):

        self.new_name = fullname
        print(self)
        print("adding new student in database ..." )

c1 = college("babalu")
print(c1.new_name)


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


class transport:
    new_truck = 1255

truck = transport()
print("new no is :",truck.new_truck)
