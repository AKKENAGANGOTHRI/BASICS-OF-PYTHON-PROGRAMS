#single and multilevel inheritence
class vehicle:
    def __init__(self):
        print("Hey..! I'm the vehicle class constructor...!")
class bike(vehicle):
    def __init__(self):
        super().__init__()
        print("Hey..! I'm the bike class constructor...!")
class superBike(bike):
    def __init__(self):
        super().__init__()
        print("Hey..! I'm the super bike class constructor...!")
s1=superBike()
print()
#hierarchial inheritence
class Engineer:
    def __init__(self):
        print("I'm the engineer class constructor")
E1=Engineer()
print("----------------------------------------------------")
class SoftwareEngineer(Engineer):
    def __init__(self):
        super().__init__()
        print("I'm the software engineer class constructor")
se1=SoftwareEngineer()
print("--------------------------------------------------")
class CivilEngineer(Engineer):
    def __init__(self):
        super().__init__()
        print("I'm the civil engineer class constructor")
c1=CivilEngineer()
print("--------------------------------------------------")
class MechanicalEngineer(Engineer):
    def __init__(self):
        super().__init__()
        print("I'm the mechanical engineer class constructor")
m1=MechanicalEngineer()
print("-----------------------------------------------------")
#combination of multiple inheritence and hierarchical inheritence(hybrid inheritence) 
class A:
    def __init__(self):
        super().__init__()
        print("class A")
class B(A):
    def __init__(self):
        super().__init__()
        print("class B")
class C(A):
    def __init__(self):
        super().__init__()
        print("class C")
class D(B,C):
    def __init__(self):
        super().__init__()
        print("class D")   
d1=D()
c1=C()