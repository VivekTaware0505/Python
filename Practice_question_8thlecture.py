# create a new file "practice.txt" using python add the following data in it 
# hi everyone
# we are learning file I/O
# using java
# i like programming in java










print("-------------------------------------- vivek learning python  -----------------------------------------------------------")



# wrtie a function replace all occurnaceof java with pyhton in above file

with open("practice.txt","r") as f:
   data = f.read()

new_data = data.replace("java","python")
print(new_data)


with open("practice.txt","w") as f:
   f.write(new_data)




print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# search if the word "learning" exists in the file or not

word = " learning "

with open("practice.txt","r") as v:
   vdata = v.read()
   if(vdata.find(word) != +1):
      print("FOUND")
   else:
      print("NOT FOUND")
