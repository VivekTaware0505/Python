# function defining and calling 

# function for adding two numbers 


def sum (a,b):
    add = a+b
    return add

print(sum(55,55))
print(sum(12,33))


# function for multiplication of two numbers 

def multi (c,d):
    multi = c*d
    return multi


print(multi(5,6))


# another type of function 


def divide (h,g):
    return h/g

print(divide(5,9))


# without parameter function 

def hallo ():
    print("hallo vivek")

hallo()


# function for calculate average of 3 numbers 

def cal_avg(p,q,r):
    sum1 = p + q + r
    avg = sum1 / 3
    return avg

print(cal_avg(98,95,97))