# Inheritance 
# when one class ( child or derived ) derives the properties and methods of another class (parent / base )

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




class carcompany:
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
    

class suzuki(carcompany):
    def __init__(self, brand):
        self.brand = brand

class ertiga(suzuki):
    def __init__(self, type):
        self.type = type

car3 = suzuki("ertiga diesel ")
car3.start()



  
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# 3 multiple inheritance 






print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# types of inheritance 
# 1 single inheritance  --  parent class and child class 
# 2 multi-level inheritance -- 1 paraent class -- 2 parent child class -- 3 child class three derived classes three properties 
# 3 multiple inheritance 

