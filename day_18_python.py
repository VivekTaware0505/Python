# recursion  

def show (n):
    if(n ==  0):
        return
    print(n)
    show(n-1)
    print("END")

show(5)


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# factorial number example in recursion 


def cal_fact(v):
    if(v == 1 or v ==0):
        return 1
    return cal_fact(v-1) * v

print(cal_fact(6))



print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# let's practice 

#  write a recursive function to calculate the sum of first n natural numbers

def sum (a):
    if (a == 0):
        return 0
    return sum(a-1) + a

cal = sum(5)
print(cal)
 
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# write a recursive function to print all element in list 
# hint : use list & index as a parameter 

def print_list(list , idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print(list,idx+1)

fruits=["mango","banana","apple","orange"]
print_list(fruits)



print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")

# Fibonacci number, where each number is the sum of the two preceding ones, starting from 0 and 1

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))