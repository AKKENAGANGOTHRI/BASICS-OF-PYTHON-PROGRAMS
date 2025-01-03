size=int(input("enter the size of the list is:"))
list=[]
for num in range(size):
    num=int(input("enter the element:"))
    list.append(num)
list.sort()
print(list)
print("the second largest number from the list is:",list[-2])

