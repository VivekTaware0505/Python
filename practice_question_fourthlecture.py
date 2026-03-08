# Q .1 store following word meaning in python dictionary
# table : "a piece of furniture ","list of facts and figures "
# cat : "a small animal"


table ={
    "table" : ["a piece of furiniture " , "list of facts and figures"],
    "cat":"a small animal"
}

print(table)


print("-------------------------------------- vivek learning python -----------------------------------------------------------")

# you are given a list of subject for student assume one classroom is required for 1 subject how many classrooms are needed by all students


subject = {
    "python","java" , "c++", "python", "javascript",
    "java", "python", "java", "c++", "c"
}

count = "we need ",len(subject) ,"classrooms"
print(subject)

print(len(subject))

print("-------------------------------------- vivek learning python -----------------------------------------------------------")

print(count)



print("-------------------------------------- vivek learning python -----------------------------------------------------------")


# write a program to enter marks of 3 subjects from the user
# and store them in a dictionary 
# start with empty dictionary & add one by one
# use subject name as key & marks as value


sub1 = int(input("enter marks of math : "))
sub2 = int(input("enter marks of science : "))
sub3 = int(input("enter marks of english : "))

dict = {}
dict.update({"math " : sub1})
dict.update({"science " : sub2})
dict.update({"english":sub3})
print(dict)