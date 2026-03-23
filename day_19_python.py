# file input/output in python 

f = open("day_two_python.py","r")
data = f.read()

print(data)
print(type(data))
f.close()


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# reading methods in file input output 


v = open("demo.txt","r")
datav = v.read(10)
print(datav)
print(type(datav))
v.close()



print("-------------------------------------- vivek learning python  -----------------------------------------------------------")

# readline method in file I/O


f= open("demo.txt","r")

line1 = f.readline()
line2 = f.readline()

print(line1)
print(line2)
print(type(line1))
f.close()


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# writing methods in file I/O

w = open("demo.txt","w")
write = w.write("we are changing the data of existing file ")

print(write)
print(type(write))
w.close()



