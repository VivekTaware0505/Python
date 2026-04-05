# static method 

# example
@staticmethod
def new_static():

    print("hallo vivek this is static mehtod ")


new_static()

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")

# car start example for ABSTRACTION in python


class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started... ")

    
car1 = car()
car1.start()
