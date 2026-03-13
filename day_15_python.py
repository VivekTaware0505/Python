# break key word in while loop __________________**********________________


b = 0

while b <= 5:
    print(b)
    if(b == 3):
        break     # break keyword is break the whole statement after get that point 
    b += 1

print (" end of loop ...")


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")



# Continue keyword in while loop


c = 0

while c <= 5:
    if(c == 3):
        c +=1
        continue # skip the condition 
    print(c)
    c += 1


# printing odd numbers using continue keyword


odd = 0

while odd <= 10 :
    if ( odd %2 == 0):
        odd += 1
        continue
    print(odd,"tthis is the odd number")

    odd += 1


    print("-------------------------------------- vivek learning python  -----------------------------------------------------------")



    # for loop 

    list = [1,2,3,5,6,4,55,4,8]

    for val in list :

        if(val == 4):
            print(val)
    else:
            print("loop end")

tup = ( 1,2,3,6,15641,512)

for num in tup:
    if ( num %2==0):
        num += 1
        print("this is the odd number -> : " ,num)
    else:
        print("end loop ")


# accessing string elements from list using for loop

veg =["tomato","ladyfingers","orange ","mango"]

for fruit in veg :
    print(fruit)
else:
    print("we print vegetables and fruits ")
     



    
