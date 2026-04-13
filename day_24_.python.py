# Inheritance 
# when one class ( child or derived ) derives the properties and methods of another class (parent / base )


# types of inheritance 
# 1 single inheritance  --  parent class and child class 
# 2 multi-level inheritance -- 1 paraent class -- 2 parent child class -- 3 child class three derived classes three properties 
# 3 multiple inheritance 



# 1 single inheritance example 

class car:
    color = "black"
    @staticmethod
    def start():
        print("car started ... ")

    @staticmethod
    def stop():
        print(" car stoped ")

    def __break(self):
        print("break fail ... ")
        
    def failbreak(self):
        self.__break()
    

class toyota(car):
    def __init__(self, name):
        self.name = name
    
    



car1 = toyota("fortuner")
car2 = toyota("innova ")

print(car1.start())
print(car1.failbreak())
print(car1.color)



print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")



# 2 multi-level inheritance -- 1 paraent class -- 2 parent child class -- 3 child class three derived classes three properties 




class carcompany:                # first class derived class 
    color = "black"
    @staticmethod
    def start():
        print("car started ... ")

    @staticmethod
    def stop():
        print(" car stoped ")

    def __break(self):
        print("break fail ... ")
        
    def failbreak(self):
        self.__break()
    

class suzuki(carcompany):         # second class 
    def __init__(self, brand):
        self.brand = brand

class ertiga(suzuki):            # third class 
    def __init__(self, type):
        self.type = type

car3 = suzuki("ertiga diesel ")
car3.start()



  
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# 3 multiple inheritance 


class A:     # base class 1
    var1 = "Welcome to class A "
    

class B:    # base class 2 
    var2 = "Welcome to class B "

class C(A, B):  # derived class 
    var3 = "Welcome to class C "
    
c1 = C()

print(c1.var1)
print(c1.var2)
print(c1.var3)







print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")




print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
