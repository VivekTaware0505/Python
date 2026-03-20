
# write a function to print the length of a list 

list1 = [1,2,3,6,65,3,35]
hallo = ["hallo ","vivek","vivek"]

def li (list):
   print(len(list))
   return

li(list1)
li(hallo)


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")



# write a function to print the elements of a list in a single line 


def singal (list):
   for item in list:
      print(item, end=" ")
      


singal(hallo)
singal(list1)



print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# write a function to the factorial of n (n is the parameter)

def cal_fact (n):
   fact = 1
   for i in range(1 , n+1):
      fact *= i
      print(fact)

cal_fact(6)



print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")





# write a function to convert USD to INR


def  converter ( usd_val):
   
  
   inr_val = usd_val * 83

   print(usd_val,"USD : ",inr_val," : INR")

converter(110)



print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# write a fonction to get input from user to know number is odd or even


def odd_even (number):
   number = int(input("enter a  number : "))
   if(number % 2 ==0):
      print("number is odd" , number)
   else:
      print("number is even")

odd_even(number='')