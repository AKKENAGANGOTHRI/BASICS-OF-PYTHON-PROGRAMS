#create a class of employee and declare the states of the class as employee name,employeeid,designation,salary,locationand special allowances
class employee:
    def __init__(self,emp_name,emp_ID,desig,sal,loc,spe_allowance):
        self.emp_name=emp_name
        self.emp_ID=emp_ID
        self.desig=desig
        self.sal=sal
        self.loc=loc
        self.spe_alloewance=spe_allowance
        print("employee name:",self.emp_name)#aceessing the values using constructor
        print("employee ID:",self.emp_ID)
        print("designation:",self.desig)
        print("employee salary:",self.sal)
        print("loaction:",self.loc)
        print("special allowances:",self.spe_alloewance)
emp1=employee("raj",1001,"HR",80000,"hyd","travel & food allowances")
print()
emp2=employee("sai",1002,"marketing",70000,"eluru","travel & food allowances")
print()
emp3=employee("scott",1003,"developer",2500,"bangore","no allowance")
print()
def employee_details(self):#accessing using function
    print("employee name:",emp1.emp_name)
    print("employee ID:",emp1.emp_ID)
    print("designation:",emp1.desig)
    print("employee salary:",emp1.sal)
    print("loaction:",emp1.loc)
    print("special allowances:",emp1.spe_alloewance)
employee_details(emp1)
'''
print("employee name:",emp2.emp_name)
print("employee ID:",emp2.emp_ID)
print("designation:",emp2.desig)
print("employee salary:",emp2.sal)
print("loaction:",emp2.loc)
print("special allowances:",emp2.spe_alloewance)'''
