# file input/output in python 

g = open("day_two_python.py","r")
data = g.read()

print(data)
print(type(data))
g.close()


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# reading methods in file input output 


v = open("demo.txt","r")
datav = v.read(10)
print(datav)
print(type(datav))
v.close()



print("-------------------------------------- vivek learning python  -----------------------------------------------------------")

# readline method in file I/O


h= open("demo.txt","r")

line1 = h.readline()
line2 = h.readline()

print(line1)
print(line2)
print(type(line1))
h.close()


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# writing methods in file I/O

# w = open("demo.txt","w")
# write = w.write("we are changing the data of existing file ")

# print(write)
# print(type(write))
# w.close()


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")




# to append data in file 

a = open("demo.txt","a")
append = a.write("we are changing the data of existing file ")

print(append)
print(type(append))
a.close()



print("-------------------------------------- vivek learning python  -----------------------------------------------------------")



# r+ method to overwrite in existing file 

t = open("demo.txt","r+")
t.write("hallo vivek")
print(t.read())
t.close()



print("-------------------------------------- vivek learning python  -----------------------------------------------------------") 
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# with syntax in file input output 

with open("demo.txt","r") as f:
    newdata = f.read()
    print(newdata)
    f.close()


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")



# overrite with method 

with open("demo.txt","w") as f:
    f.write("we put it some new data")  




print("-------------------------------------- vivek learning python  -----------------------------------------------------------")

# deleting file method in file I/O

import os 

os.remove("sample.txt")
