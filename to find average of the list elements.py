size=int(input("enter the size of the list is:"))
list=[]
for num in range(size):
    num=int(input("enter the element:"))
    list.append(num)
print(list)
average=(sum(list)/len(list))
print("the average of the ",list," is:",average)