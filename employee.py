# to read the employee name,designation,salary,special allowances,bonus as input from the user 
#gross monthly salary
emp_name=input("employee name:")
designation=input("designation:")
special_allowance=int(input("special_allowances:"))
salary=int(input("salary:"))
bonus=int(input("bonus:"))
GMS=salary+special_allowance
GAS=(GMS*12)+bonus
print("gross monthly salary:",GMS)
print("gross annually salary:",GAS)
tax_inc=0
if(salary>500000):
    tax_inc=GAS*0.15
    print("taxable_income:",GAS-tax_inc)
elif(salary>400000):
    tax_inc=GAS*0.10
    print("taxable_income:",GAS-tax_inc)
else:
    tax_inc=GAS*0.2
    print("taxable_income:",GAS-tax_inc)
                  