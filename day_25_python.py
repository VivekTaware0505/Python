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
