#write a program to check the entered by the user is odd or even

num = int(input("enter number to check no is odd or even : "))



if(num % 2 == 0 ):
    print("number is EVEN ")
else:
    print("number is ODD ")


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