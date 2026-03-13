  # print the elements of the following list using a loop

# list =[1,4,9,16,25,36,49,64,81,100]
 

# for element in list:
#     print(element)
# else:
#     print("END")


# search for a number x in this tuple using loop


tup = (1,4,9,16,25,36,49,64,81,100,81,36)

x = 36
idx = 0

for num in tup:
    if(num == x):
        print("we found x ->:", num ,":",idx )
    idx += 1
      
    