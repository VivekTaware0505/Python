#write a program to check the entered by the user is odd or even

num = int(input("enter number to check no is odd or even : "))



if(num % 2 == 0 ):
    print("number is EVEN ")
else:
    print("number is ODD ")


print("-------------------------------------------------------VIVEK------------------------------------------------------------")


# write a program to find the greatest of 3 numbers entered bye the user

a = int(input("enter first number : "))
b = int(input("enter second number : "))
c = int(input("enter third number : "))

if(a >= b and b >= c):
   print("first number is largest : " , a )
elif(b >= c):
   print("second number is largest : " , b)
else:
  print("third number is largest : ", c)


print("-------------------------------------------------------VIVUQCYdXT16Xxzr1qCSVxxntce0-UYXmcqJ_aodkoq39Fv2E6f--------------")

# write a program to find the grestest of 4 number enetered by the user

x = int( input("enter first number : "))
y = int(input("enter second number : "))
z = int(input("enter third number : "))
d = int(input("enter fourth number  : "))

if(x >= y and y >= z):
    print("first number is largest : " , x)
elif(y >= z and z >= d):
    print("second number is largest : " , y)
elif(z >= x and x >= d):
    print("third number is largest : " , z)
else:
    print("fourth number is lagest : " , d)

    
print("-------------------------------------------------------VIVUQCYdXT16Xxzr1qCSVxxntce0-UYXmcqJ_aodkoq39Fv2E6f--------------")

# write a program if a number is multiple of 7 or not 

num = int(input("enter number to check"))

if(num % 7 ==0):
    print(" number is multiple by 7 : " , num)
else:
    print("not multiple bye 7 : " , num)


# or not multiple bye 5 

num2 = int(input("enter number to check "))

if(num2 % 5 ==0):
    print("multiple by 5 : " , num2)
else:
    print(num2 , "is not multiple by 5 ")