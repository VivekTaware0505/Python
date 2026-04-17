# Polymorphism :- Operator Overloading 
# when the same operator is allowed to have different meaning to the context 

# example of polymorphism 

print(1+2) # its trying to additon 
print("vivek" + "taware") # its trying to concatenet 
print([1, 2, 3] + [4, 5, 6])  # its trying to merge

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")

# complex numbers example 


class complex:
    def __init__(self, real, img):
        self.real = real 
        self.img = img 

    def shownumber(self):
        print(self.real, "i +", self.img,"j")

    def __add__(self, num2 ):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return complex(newreal, newimg)
    

    def __sub__(self, num2 ):
        newreal = self.real - num2.real
        newimg = self.img - num2.img
        return complex(newreal, newimg)
    
num1 = complex(1, 3)
num1.shownumber()

num2 = complex(4,5)
num2.shownumber()

print("printing the addition of complex in :")

num3 = num1 + num2
num3.shownumber()
        
print(" printing the substraction of two numbers : ")

num3 = num1 -  num2 
num3.shownumber()

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# opeators and Dunder Functions 

# a+b -> addition :-  1)  __add__(b)
# a-b -> substraction :- 2) __sub__(b)
# a*b -> multiplication :- 3) __mul___(b)
# a/b -> divide   :- 4) __truediv____(b)
# a%b -> addition  :- 5) __mod____(b)

