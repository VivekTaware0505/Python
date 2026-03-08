# practice questions

# write a program to ask the user to enter names of their 3 favorite movies and stores them in a list 

movie_name1 = input("enter movie names : ")
movie_name2 = input("enter movie names : ")
movie_name3 = input("enter movie names : ")


M_list2 = []
M_list2.append(input("enter movie names : "))
M_list2.append(input("enter movie names : "))
M_list2.append(input("enter movie names : "))
print(M_list2)
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


M_list = []
M_list1 = []



M_list.append(movie_name1)
M_list.append(movie_name2)
M_list.append(movie_name3)
print(M_list)
 
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


M_list1.insert(0,movie_name1)
M_list1.insert(1,movie_name2)
M_list1.insert(2,movie_name3)
print(M_list1)


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# write a program to to count the number of students with the A grade in the following tuple

grade_tup =("C","D","A","A","B","B","A")  

print(grade_tup.count("A"))


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# write a peogram to check if a list contains a palindrome of element (hint : use cop() method)
# [1,2,3,2,1]   [1, "abc" , "abc" , 1]

list1 = [12,2,2]


copy_list = list1.copy()
copy_list.reverse()

if(copy_list == list1):
    print("is a palindrome ")
else:
    print("is not palindrome")


    # store the below values in a list and sort them from "A" to "D"
    #["C","D","A","A","B","B","A"]


grade = ["C","D","A","A","B","B","A"] 
grade.sort()
print(grade)
