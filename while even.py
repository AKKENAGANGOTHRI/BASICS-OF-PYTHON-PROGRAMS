num=int(input("enter the integer value:"))
evendigitcount=0
rem=0
#condition to get number of even digits
while(num!=0):
    rem=num%10
    if(rem%2==0):
        evendigitcount+=1
    num=num//10
print("number of even digits are",evendigitcount)