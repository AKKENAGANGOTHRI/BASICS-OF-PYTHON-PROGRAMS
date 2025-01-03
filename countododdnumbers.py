#to print the count of odd numbers  from 1 to n
num=int(input("enter the number:"))
oddcount=0
for i in range(1,num+1):
    if(i%2!=0):
        oddcount+=1
print("count of odd numbers from 1 to",num,":",oddcount)
