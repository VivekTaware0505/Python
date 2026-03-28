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

def check_word ():
   word = " learning "

   with open("practice.txt","r") as v:
      vdata = v.read()
      if(vdata.find(word) != +1):
         print("FOUND")
      else:
         print("NOT FOUND")


check_word()


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
 
# write a function to findin which line of the file does the word "learning" occure first print -1 if word not found 


def check_for_line():
   nword = "learning"
   ndata = True
   lineno = 1
   with open("practice.txt","r") as n:
      while ndata:
         ndata = n.readline()
         if(nword in ndata):
            print(lineno)
         lineno += 1


check_for_line()


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# from a file containing numbers seperated by comma print the count of even numbers    

with open("demo.txt","r") as t:
   tdata = t.read()
   print(tdata)

   num = ""
   for i in range(len(tdata)):
      if(tdata[i] == ","):
         print(int(num))
         num = ""
      else:
         num += tdata[i]

