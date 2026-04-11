# Inheritance 
# when one class ( child or derived ) derives the properties and methods of another class (parent / base )

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


# types of inheritance 
# 1 single inheritance 
# 2 multi-level inheritance 
# 3 multiple inheritance 

