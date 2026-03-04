# dictionary in python 

print("-------------------------------------- vivek learning pyhton -----------------------------------------------------------")

info = {
    "name" :"vivek",
    "subjects" : "java",
    "marks" : 76
}
print(info)

info["name"]= "akshay"
info["surname"]="thorat"
print(info)

print("-------------------------------------- vivek learning pyhton -----------------------------------------------------------")

info_new = {
    "names": ["vivek","akshay"],
    "marks": (60,76)
}
info_new["topics"]="learnig","analysis" # this means overrite the that point 
info_new["locatin"] ="malinagar",5,"ganeshgao",15
info_new["vehicle name"] = input("enter your vehicle name : ")
info_new["percentage"] = 60.80,6.80
print(info_new)
print(type(info_new))
print(info_new["marks"])

print("-------------------------------------- vivek learning pyhton -----------------------------------------------------------")


# empty dictionary creating

empty_dict = {}

print(type(empty_dict))
empty_dict["where are you going "] = "i am going to canada"
print(empty_dict)


print("-------------------------------------- vivek learning pyhton -----------------------------------------------------------")

# nasted dictionary a dictionary having inside another dictionary

student = {
    "name" : "vivek taware",
    "subjects" :{
        "java" : 99,
        "pyhton" : 99,
        "c" : 99
    }
}
print(student)