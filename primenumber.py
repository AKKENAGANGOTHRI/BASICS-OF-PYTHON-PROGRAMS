#condition to check the number is prime number or not
num=int(input("enter the number: "))
count=0
for i in range(1,num+1):
    if(num%i==0):
        count+=1
if(count==2):
    print("prime number")
else:
    print("not a prime number")
#------------------------------------------------ 
for i in range(2,num):
    if(num%i==0):
        print("not a prime number")
        break
else:
    print("prime number") 