# create a new file "practice.txt" using python add the following data in it 
# hi everyone
# we are learning file I/O
# using java
# i like programming in java

with open("practice.txt","w") as f:
  data =  f.write("hi everyone \nwe are learning file i/o\nusing java\ni like programming in java")
print(data)