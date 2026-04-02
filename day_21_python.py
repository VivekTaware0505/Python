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

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# Methods In class and Object 


class school:
    school_name = "vivek's college"

    def __init__(self, sname,smark):
        self.sname = sname
        self.smark = smark

        def welcome(self):
            print("welcome students .....")
        
        def get_mark(self):
            return self.mark
        
v1 = school("vivek",99)
v1.welcome()
print(v1.get_mark())
        

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
