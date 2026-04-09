# del keyword used to delete object properties and delete object itself 

class Student:

    def __init__(self, name):
        self.name = name

s1 = Student("Vivek")
print(s1.name)


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# Private (like) attribute and methods 
# conceptual implementation in python
# private attribute and methods are meant to be used only within the class and are not accessible for outside the class 





class new_Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def __calculate_average(self):
        return sum(self.__marks) / len(self.__marks)

    def get_result(self):
        avg = self.__calculate_average()
        return avg


ss1 = new_Student("Vivek", [80, 90, 85])
print(ss1.get_result())