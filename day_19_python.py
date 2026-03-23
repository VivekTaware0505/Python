# file input/output in python 

f = open("day_two_python.py","r")
data = f.read()

print(data)
print(type(data))
f.close()




# reading methods in file input output 


v = open("demo.txt","r")
datav = v.read(10)
print(datav)
print(type(datav))
v.close()