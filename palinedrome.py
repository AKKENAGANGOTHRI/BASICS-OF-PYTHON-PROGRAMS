# to print the integer is palindrome or not
num=int(input("enter the number:"))
rev=0
rem=0
temp=num
while(num!=0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
if(temp==rev):
    print(temp,"is a palinedrome number")
else:
    print(temp,"is  not a palinedrome number")