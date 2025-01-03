num=int(input("enter the number:"))
rev=0
rem=0
temp=num
for i in range(2,num):
    if(num%i==0):
        print("not a prime palinedrome number")
        break
else:
    while(num!=0):
        rem=num%10
        rev=rev*10+rem
        num=num//10
    if(temp==rev):
        print(temp,"is a prime palinedrome number")
    else:
        print(temp,"not a prime palinedrome number")
