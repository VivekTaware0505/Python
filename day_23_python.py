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

# example no -1

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

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")

# example no - 2 

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def __update_balance(self, amount):
        self.__balance += amount

    def deposit(self, amount):
        self.__update_balance(amount)
        return self.__balance


acc = BankAccount(1000)
print(acc.deposit(500))

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# example no -3 

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def __bonus(self):
        return self.__salary * 0.10

    def total_salary(self):
        return self.__salary + self.__bonus()


e1 = Employee(20000)
print(e1.total_salary())

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


