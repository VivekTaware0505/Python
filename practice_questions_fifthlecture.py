# print numbers from 1 to 100 

i = 1

while i <= 100:
    print(i)
    i+=1

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


v = 100

while v >= 1:
    print(v)
    v-=1
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")

# print the multiplication table of a number n 

n = int(input("enter number : "))
s = 1
while s<=10 :
    print(n*s)
    s += 1

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# pritn the following elements from list using loop
# [1,4,9,16,25,36,49,64,81,100]


nums = [1,4,9,16,25,36,49,64,81,100]

idx = 0

while idx < len(nums) : 
    print(nums[idx])   # idx is printing the index number wise list elements 
    idx +=1 

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# search for a number X in this tuple using loop
# (1,4,9,16,25,36,49,64,81,100)

tup = (1,4,9,16,25,36,49,64,81,100)
x = 36
xy = 0

while xy < len(tup):
    if(tup[xy] ==  x ):
        print("FOUND ",tup[xy])
   
    xy += 1