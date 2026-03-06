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
print(list(subject.values()))