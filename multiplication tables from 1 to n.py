# to print multiplication tables from 1 to n
num=int(input("enter the number:"))
print("multiplication table  of",num,":")
for i in range(1,num+1):
    for j in range(1,11):
        print(i,"x",j,"=",i*j)
