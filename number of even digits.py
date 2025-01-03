#to print number of even digits present in given integer
num=int(input("enter the number:"))
rem=0
evendigitcount=0
while(num!=0):
    rem=num%10
    if(rem%2==0):
        evendigitcount=evendigitcount+1
    num=num//10
print("number of even digits are",evendigitcount)