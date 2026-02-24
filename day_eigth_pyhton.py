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


    # finding grade using contional statements


grade = int(input("enter your marks get grades : "))

if(grade>=90):
    print("you got grade :A: ")
elif(grade>= 80 and grade < 90):
    print("you got grade :B: ")
elif(grade>= 70 and grade < 80):
    print("you got grade :C: ")
elif(grade>= 60 and grade < 70):
    print("you got grade :D: ")
else:
    print("you are fail")

    # new 
marks = int(input("enter students marks : "))

if(marks >= 90):
    g = "A"
elif(marks >= 80 and marks < 90 ):
    g ="B"
elif(marks >= 70 and marks < 80):
    g = "C"
else:
    g = 'D'

print("students grade -> : ", g)


# nested if statements using nested if finding the candidate was able to lead election or not

election_age = int(input("enter your agr to know : "))

if(election_age >= 21):
    if(election_age >= 80):
        print("your age is paased for election")
    else:
        print("you can lead elections")
else:
    print("you not fill form")