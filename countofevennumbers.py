#to print the count of even numbers  from 1 to n
num=int(input("enter the number:"))
evencount=0
for i in range(1,num+1):
    if(i%2==0):
        evencount+=1
print("count of even numbers from 1 to",num,":",evencount)
