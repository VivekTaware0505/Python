# condotional statements if elif else 

age = int(input("enter your age : "))

if(age>=18):
    print("you can vote")
else:
    print("you are not eligible for vote")

    # traffic light example for if and elif

light = input("enter light colour : ")

if(light == "green"):
    print("safe you can go now")
elif(light == "red"):
    print("wait for green light")
elif(light == "yellow"):
    print("look and go slow")
else:
    print("light is broken")