size=int(input("enter the size if the list:"))
list=[]
for i in range(size):
    list.append(input("enter the elements:"))
print("the ascending order of list is:",sorted(list))
print("the descending order of list is:",sorted(list,reverse=True))
