# range() in python 

seq = range(5)

print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


for i in seq:
    print(i)


    print("-------------------------------------- vivek learning python only (start)  -----------------------------------------------------------")


for a in range(10): # only starting
    print(a)

print("-------------------------------------- vivek learning python (start,stop) -----------------------------------------------------------")

for b in range(2,10): # (start , stop ) point has marked
    print(b)


print("-------------------------------------- vivek learning python  (start , stop . step )-----------------------------------------------------------")


for c in range(3,10,2):  # (start, stop , step) starting and stop and step is pointed step is pointed for increasing count 
    print(c)



print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# even number using range in python 

for e in range(2,100,2):
    print(e,"is even")


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")

# odd numbers using range in python

for o in range (1 , 100,2):
    print(o,"is odd")



print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# pass statement 


for p in range(10):
    pass


print("we pass the above statement")