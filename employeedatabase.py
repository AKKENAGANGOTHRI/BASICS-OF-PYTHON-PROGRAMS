list=[("david","sales",60000),("taylor","marketing",70000),("jackson","it",80000),("ava garcia","hr",65000),("sophia patel","sales",75000)]
department=["sales","marketing","it","hr","sales"]
salaries=[60000,70000,80000,65000,75000]
print(list)           
list.append(("scott","marketing",80000))
print(list)
print("after remove the employee is:")
names=["david","taylor","jackson","ava garcia","sophia patel","scott"]
names.remove("david")
print(names)
department=["sales","marketing","it","hr","sales","marketing"]
print("sort the employee by department: ",sorted(department))
print(department)
salaries=[60000,70000,80000,65000,75000,80000]

