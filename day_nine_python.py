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


# list slicing in python


new_marks = [10,20,30,40,50,60,70]

print(new_marks[1:4])
print(new_marks[:5])
print(new_marks[1:])
print(new_marks[-4:-1]) # this is the reverse string so access it bye reverse way
print(new_marks[-5])
