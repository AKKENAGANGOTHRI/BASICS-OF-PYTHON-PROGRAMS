#to print prime numbers from 1 to n
num=int(input("enter the number: "))
for i in range(2,num+1):
    for j in range(2,i):
        if(i%j==0):
           break 
    else:
        print(i)