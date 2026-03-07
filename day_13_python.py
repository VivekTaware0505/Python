# set in python 
        # set is the collection of unorderd items 

collection ={1,2,3,4}

print(collection)
print(type(collection))


print("-------------------------------------- vivek learning pyhton -----------------------------------------------------------")


collection1 = {"hallo", 1 , 2,2,2,"world","world"}

print(collection1)  # in the set he ignores the duplicate items and prints only once
print(len(collection1))



print("-------------------------------------- vivek learning pyhton -----------------------------------------------------------")



collection3 = set()

collection3.add("vivek")
collection3.add(90)
collection3.add(556)

print(collection3)

collection3.remove(556)
collection3.add((1,2,3,4))

print(collection3)
print("-------------------------------------- vivek learning pyhton after clear method-----------------------------------------------------------")


collection3.clear()
print(len(collection3))
print(collection3)

print("-------------------------------------- vivek learning pyhton pop method -----------------------------------------------------------")


# pop method 

new_cl ={ "vivek ", "taware" , "malinagar" , "hallo",1,2,3,}

print(new_cl)

print("-------------------------------------- vivek learning pyhton pop method -----------------------------------------------------------")


print(new_cl.pop())  # he shows in the output what he romoves from set

print("-------------------------------------- vivek learning pyhton pop method -----------------------------------------------------------")


print(new_cl.pop())