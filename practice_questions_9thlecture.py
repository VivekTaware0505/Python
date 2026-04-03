# create student class that makes name and marks of 3 subject as argument in constructor 
# then create a method to print the avrage



class student:

    def __init__(self, marks, name):
        self.marks = marks
        self.name = name

    def get_avg(self):
        total = 0
        for val in self.marks:
            total += val
        print("Hello", self.name, "your avg is:", total / len(self.marks))


s1 = student([97, 98, 99], "vivek")   # ✔ correct order
s1.get_avg()

s1.name = " babalu "
s1.get_avg()

print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
