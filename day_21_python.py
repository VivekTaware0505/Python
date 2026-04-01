# class and intance atrribute 

class Student:
    college_name = "ABC College "
    name = "Vivek"

    def __init__(self,name,mark):
        self.name = name
        self.mark = mark

        print("adding student in Databse...")

s1 = Student("babalu",97)
print(s1.name,s1.mark)