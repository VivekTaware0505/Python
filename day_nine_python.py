# tuples and list lecture No : 03
# lists are mutable means changeble 

student_data = ["vivek", 60,55 ,"malinagar"]

print(student_data[0])
print(len(student_data))
print(type(student_data))
student_data [0] = "akshay"
print(student_data)
print(student_data[0:3])


marks = [ 99.5,98.2,65.2,78.2,98.5]
print(marks)
print(marks[0])

print("---------------------------------------end line-----------------------------------------------------")


# list slicing in python


new_marks = [10,20,30,40,50,60,70]

print(new_marks[1:4])
print(new_marks[:5])
print(new_marks[1:])
print(new_marks[-4:-1]) # this is the reverse string so access it bye reverse way
print(new_marks[-5])


print("------------------------------------------end line--------------------------------------------------")

# list methods 

#append and sort method

list = [4,5,3,1,2,6]

print(list)
list.append(9)

print("-----------------------------------------end line---------------------------------------------------")

print(list)
print(list.sort()) # returnt none value to see the value we print it and after print this on 
                      # next time he prints ascending orde of list
print(list)

print("----------------------------------------- end line---------------------------------------------------")

# revese sort in list method

list.sort(reverse=True) # true function in python is always define with first letter is capital like "True "
print(list)

print("---------------------------------------end line -----------------------------------------------------")

list.reverse()
print(list)

print("--------------------------------------end line------------------------------------------------------")

list.insert(8,22)
print(list)

print("---------------------------------------end line-----------------------------------------------------")
# string sorting in list slicing

fruit = ["banana","orange","apple"]

print(fruit) # before sorting 

fruit.sort()

print(fruit) # after sorting
print("--------------------------------------end line ------------------------------------------------------")