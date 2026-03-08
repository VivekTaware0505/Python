# Dictionary methods 
info = {
    "name" :"vivek",
    "subjects" : "java",
    "marks" : 76
}

print(info.keys())


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")

# type casting in dictionary we can change dictionary into list and tuple

print(list(info.keys()))
print(tuple(info.keys()))



print(len(info)) # print total value of key pairs

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


print(info.values()) #values method it returns all value pairs into tuples
print(info.get("name")) # returns the key according to value

# when in the get method put the element or that key it doesnt exixts in our program that time the method give us """ none value"""
#and execute the next line code thats whya that method are used in python 


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")

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

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


print(list(subject.values()))
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")

print(subject.items())

pairs = list(subject.items())
print(pairs[0])
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")

print(pairs[2])


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


new_dict = {"name5":"hallo"}
subject.update(new_dict)
print(subject)

print("-------------------------------------- vivek learning pyhton -----------------------------------------------------------")


subject.update({"name4": " shraddha"})
print(subject)

