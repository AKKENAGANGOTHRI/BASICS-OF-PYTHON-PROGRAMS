class student:
    def __init__(self):
        print("object is created")
        #direct intialization and this is non parameterized constructor
        self.name="kavya"
        self.age=22
#object creation
std1=student()
print(std1) 
std2=student()
print(std2)
print("=========================================")
std3=student()
print("student name:",std3.name)
print("student age:",std3.age)
print("------------------------------")
std4=student()
print("student name:",std4.name)
print("student age:",std4.age)
print("===========================================")
