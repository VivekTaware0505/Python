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


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")

# create account class with 2 attributes - balance and account no 
# create method for debit , credit and printing the balance 


class Account:
    def __init__(self, bal , ac):
        self.balance = bal
        self.account = ac

    def debit(self, amount):
        self.balance -= amount
        print(" Rs . ", amount, " has debited")
        print(" total balance = ", self.get_balance())


    def credit(self, amount):
        self.balance += amount
        print(" Rs. ", amount, " was credit ")
        print(" total balance = ", self.get_balance())
        

    def get_balance(self):
        return self.balance
    

ac1 = Account(15000, 121201)
ac1.debit(500)
ac1.credit(200000)


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")

