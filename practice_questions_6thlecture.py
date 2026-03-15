  # print the elements of the following list using a loop

list =[1,4,9,16,25,36,49,64,81,100]
 

for element in list:
    print(element)
else:
    print("END")


 
 
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# search for a number x in this tuple using loop


tup = (1,4,9,16,25,36,49,64,81,100,81,36)

x = 36
idx = 0

for num in tup:
    if(num == x):
        print("we found x ->:", num ,":",idx )
    idx += 1
      
    

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# using for & range print numbers 1 to 100 


for w in range(1,101):
    print(w)



print("-------------------------------------- vivek learning python  -----------------------------------------------------------")

# print numbers from 100 to 1

for r in range(100, 1,-1):
    print(r)
  

    

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# print multiplication table of number n


n = 8

for g in range(1,11):
    print(g*n)