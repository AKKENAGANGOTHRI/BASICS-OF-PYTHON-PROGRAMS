size=int(input("enter the size of the list is:"))
list=[]
positive_num=[]
negative_num=[]
for num in range(size):
    num=int(input("enter the element:"))
    list.append(num)
for num in list:
    if(num>=0):
        positive_num.append(num)
    else:
        negative_num.append(num)
print("the user entered list is:",list)
print("the positive numbers of the ",list,"are:",positive_num)
print("the positive numbers of the ",list,"are:",negative_num)
