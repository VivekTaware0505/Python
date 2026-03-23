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

datac = f.readline()

print(datac)
print(type(datac))
f.close()