# practice questions

# write a program to ask the user to enter names of their 3 favorite movies and stores them in a list 

movie_name1 = input("enter movie names : ")
movie_name2 = input("enter movie names : ")
movie_name3 = input("enter movie names : ")

M_list = [""]
M_list.insert(0,movie_name1)
M_list.insert(1,movie_name2)
M_list.insert(2,movie_name3)
print(M_list)


# write a program to to count the number of students with the A grade in the following tuple

grade_tup =("C","D","A","A","B","B","A")  

grade_tup.count("A")
print(grade_tup)