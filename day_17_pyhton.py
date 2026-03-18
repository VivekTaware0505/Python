# function defining and calling 

# function for adding two numbers 


def sum (a,b):
    add = a+b
    return add

print(sum(55,55))
print(sum(12,33))

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")

# function for multiplication of two numbers 

def multi (c,d):
    multi = c*d
    return multi


print(multi(5,6))

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")

# another type of function 


def divide (h,g):
    return h/g

print(divide(5,9))

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")

# without parameter function 

def hallo ():
    print("hallo vivek")

hallo()

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")

# function for calculate average of 3 numbers 

def cal_avg(p,q,r):
    sum1 = p + q + r
    avg = sum1 / 3
    return avg
 
print(cal_avg(98,95,97))




def vivek ():
    print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
    return

# print function 
# two types of function built-in function and user define function

# built function 

print(" hallo vivek ", end="we not breaking the line ")  # usually in print function he automatically break the line but in that case we change the function commads
print("hallo wolrd " , " hallo india " ,sep="🙏"  ) # we also change function and removed gap from two string and add namste symbol


vivek()


# default parameter

def multi_new(num1 = 10, num2 = 10):
        print(num1 * num1)
        return 

multi_new()
