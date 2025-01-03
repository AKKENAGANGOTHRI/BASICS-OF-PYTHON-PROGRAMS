class student:
    def __init__(self,name,age):
        print("object is created")
        # this is  parameterized constructor
        self.name= name
        self.age= age
std1=student("krishna",20)
print("student name:",std1.name)
print("student age:",std1.age)
print("------------------------------")
std2=student("radha",19)
print("student name:",std2.name)
print("student age:",std2.age)