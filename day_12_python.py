# Dictionary methods 
info = {
    "name" :"vivek",
    "subjects" : "java",
    "marks" : 76
}

print(info.keys())


print("-------------------------------------- vivek learning pyhton -----------------------------------------------------------")

# type casting in dictionary we can change dictionary into list and tuple

print(list(info.keys()))
print(tuple(info.keys()))



print(len(info)) # print total value of key pairs

print("-------------------------------------- vivek learning pyhton -----------------------------------------------------------")


print(info.values()) #values method it returns all value pairs into tuples
print(info.get("name")) # returns the key according to value

# when in the get method put the element or that key it doesnt exixts in our program that time the method give us """ none value"""
#and execute the next line code thats whya that method are used in python 


print("-------------------------------------- vivek learning pyhton -----------------------------------------------------------")

subject = {

    "math":99,
    "java":99,
    "pyhton":99,
    "names":{

        "name 1":"vivek",
        "name 2" :"akshay",
        "name 3" : "vaibhav"

    }
}

print(subject.get("pyhton"))

print(subject["names"])

print("-------------------------------------- vivek learning pyhton -----------------------------------------------------------")


print(list(subject.values()))
print("-------------------------------------- vivek learning pyhton -----------------------------------------------------------")

print(subject.items())

pairs = list(subject.items())
print(pairs[0])
print("-------------------------------------- vivek learning pyhton -----------------------------------------------------------")

print(pairs[2])