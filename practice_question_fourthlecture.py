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




print("-------------------------------------- vivek learning python -----------------------------------------------------------")
print("-------------------------------------- vivek learning python -----------------------------------------------------------")


# figure out a way to store 9 and 9.0 as separate values in the set 
# you can take the help of the built in data types 


values ={ 9,9.0} # this operation in the python as considered as the values are same so he prints only 9
 
 # method no 1 to solve that problem 

value = { 9 , "9.0"}
print(value)

# method no 2

set_value = {
     
    ("int",9),
    ("float",9.0)

}
print(set_value)