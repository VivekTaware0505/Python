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
 


# write a recursive function to print all element i list 
# hint : use list & index as a parameter 

def print_list(list , idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print(list,idx+1)

fruits=["mango","banana","apple","orange"]
print_list(fruits)